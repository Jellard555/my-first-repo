# -*- coding: UTF-8 -*-
import csv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

# 填充大学列表函数（优化数据提取逻辑）
def fillUnivList(html, ulist):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all("tr")
    for tr in rows:
        # 排名：优先通过class定位，容错处理
        rank_elem = tr.find("div", class_="ranking")
        rank = rank_elem.get_text(strip=True) if rank_elem else ""
        
        # 名称：中文+英文
        name_cn_elem = tr.find("span", class_="name-cn")
        name_cn = name_cn_elem.get_text(strip=True) if name_cn_elem else ""
        name_en_elem = tr.find("span", class_="name-en")
        name_en = name_en_elem.get_text(strip=True) if name_en_elem else ""
        
        # 层次（标签）
        level_elem = tr.find("p", class_="tags")
        level = level_elem.get_text(strip=True) if level_elem else ""
        
        # 省市、类型、分数：通过class/属性定位，而非固定索引
        city_elem = tr.find("td", attrs={"data-v-2e3c901a": "", "data-v-7e532e70": ""})  # 适配网页实际属性
        city = city_elem.get_text(strip=True) if city_elem else ""
        type_elem = city_elem.find_next_sibling("td") if city_elem else None
        type_univ = type_elem.get_text(strip=True) if type_elem else ""
        score_elem = type_elem.find_next_sibling("td") if type_elem else None
        score = score_elem.get_text(strip=True) if score_elem else ""
        score2_elem = score_elem.find_next_sibling("td") if score_elem else None
        score2 = score2_elem.get_text(strip=True) if score2_elem else ""
        
        ulist.append([rank, name_cn, name_en, level, city, type_univ, score, score2])

# 保存到CSV函数（优化编码和空值处理）
def saveToCSV(ulist, filename):
    headers = ['排名', '中文名', '英文名', '层次', '省市', '类型', '总分', '分项分']
    # 过滤全空行+排名为空的行
    filtered_ulist = [row for row in ulist if any(row) and str(row[0]).strip()]
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(filtered_ulist)

# 安全的元素操作函数（替换原死循环）
def safe_click(driver, locator, timeout=10):
    """
    安全点击元素：等待元素可点击，超时返回False
    :param driver: 浏览器驱动
    :param locator: 定位器元组 (By.XXX, "value")
    :param timeout: 超时时间
    :return: 是否点击成功
    """
    try:
        elem = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        elem.click()
        time.sleep(1)  # 点击后短等待
        return True
    except (TimeoutException, StaleElementReferenceException):
        print(f"元素{locator}定位失败/不可点击")
        return False

if __name__ == "__main__":
    url = "https://www.shanghairanking.cn/rankings/bcur/2026"
    start = time.strftime("%H:%M:%S", time.localtime())
    
    # 配置浏览器选项（兼容Chrome/Edge，无界面模式可选）
    options = webdriver.Chrome()
    # options.add_argument("--headless")  # 无界面模式（注释掉则显示浏览器）
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    
    # 初始化变量
    actions = ActionChains(driver)
    ulist = []
    page_num = 1  # 记录当前页码
    
    try:
        while True:
            print(f"正在抓取第{page_num}页数据...")
            # 等待页面核心内容加载完成
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ranking"))
            )
            
            # 抓取当前页数据
            html = driver.page_source
            fillUnivList(html, ulist)
            
            # 滚动到底部，等待新内容加载
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            # 定位下一页按钮（修正后的定位方式）
            next_page_locator = (By.CSS_SELECTOR, "li.next-page")  # 适配实际网页的下一页按钮class
            # 尝试点击下一页，失败则退出循环（无下一页）
            if not safe_click(driver, next_page_locator):
                print("已抓取到最后一页，停止翻页")
                break
            
            page_num += 1
            # 防反爬：随机短等待（可选）
            # time.sleep(random.uniform(1, 3))
    
    except Exception as e:
        print(f"程序执行异常：{str(e)}")
    finally:
        # 关闭浏览器
        driver.quit()
        end = time.strftime("%H:%M:%S", time.localtime())
        print(f"抓取完成！用时：{start} - {end}，共抓取{page_num}页，{len(ulist)}条数据")
        
        # 保存CSV
        saveToCSV(ulist, 'university_rankings.csv')
        print("数据已保存到 university_rankings.csv")