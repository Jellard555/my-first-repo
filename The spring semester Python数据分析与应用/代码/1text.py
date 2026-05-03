# -*- coding: UTF-8 -*-
# 导入相关库
import csv
from bs4 import BeautifulSoup
import bs4
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标操作
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# 填充大学列表函数,代码可优化
def fillUnivList(html, ulist):
    soup = BeautifulSoup(html, 'html.parser')
    # 先定位到排名表格，再找tbody里的有效数据行
    table = soup.find("table", class_="rk-table")
    rows = table.find("tbody").find_all("tr") if table and table.find("tbody") else []
    for tr in rows:
        # 初始化所有字段，避免索引错误
        rank = ""
        name_cn = ""
        name_en = ""
        t1 = ""
        city = ""
        t2 = ""
        score = ""
        score2 = ""
        #排名
        div_rank = tr.find("div",class_="ranking")
        if div_rank:
            rank = div_rank.get_text(strip=True)
        name_elem1 = tr.find("span", class_="name-cn")
        if name_elem1:
            name_cn = name_elem1.get_text(strip=True)
        name_elem2 = tr.find("span", class_="name-en")
        if name_elem2:
            name_en = name_elem2.get_text(strip=True) 
        type_elem = tr.find("p", class_="tags")
        if type_elem:
            t1 = type_elem.get_text(strip=True)
        tds = tr.find_all("td")
        if len(tds) >= 6:
            city = tds[2].get_text(strip=True) 
            t2 = tds[3].get_text(strip=True) 
            score = tds[4].get_text(strip=True)
            score2 =  tds[5].get_text(strip=True) 
        # 添加到列表
        if name_cn:
            ulist.append([rank,name_cn,name_en,t1,city,t2,score,score2])


# 保存到CSV函数
def saveToCSV(ulist, filename):
    filepath = os.path.abspath(filename)
    dir_path = os.path.dirname(filepath)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    headers = ['排名', '中文名', '英文名', '层次','省市','类型','总分','分项分']
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(ulist)
    print(f"csv文件已经生成:{filepath},一共{len(ulist)}行数据")
# 鼠标操作运行函数
# 把原来的action_run函数，替换成这个safe_next_page函数
def action_run(driver, actions, info, by=By.ID, time_num=1):
    while 1:
        config_facesearch = driver.find_element(by=by, value=info)
        if config_facesearch.is_displayed():
            actions.move_to_element(config_facesearch).click().perform()
            time.sleep(time_num)
            break
        else:
            print("%s is not find, waiting..." % (info))
            time.sleep(2)




# 主函数

if __name__ == "__main__":
    url = "https://www.shanghairanking.cn/rankings/bcur/2026"
    start = time.strftime("%H:%M:%S", time.localtime())
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options) #需要根据浏览器类型修改，浏览器需设置远程操作
    driver.maximize_window()
    driver.get(url)
    wait = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "rk-table"))
    )
    time.sleep(2)

    "模拟鼠标操作"
    actions = ActionChains(driver)
    ulist = []
    page = 1
    
    for i in range(20):
        html = driver.page_source
        fillUnivList(html, ulist)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 滚动至底部
        action_run(driver, actions, info="li[title='下一页']", by=By.CSS_SELECTOR)


    
    # 统计时长+关闭浏览器（移到循环外，避免提前关闭）
    end = time.strftime("%H:%M:%S", time.localtime())
    print(f"开始时间：{start}，结束时间：{end}")
    driver.quit()

    # 过滤空值并保存CSV
    new_ulist = [row for row in ulist if row[0] and str(row[0]).strip() != ""]
    saveToCSV(new_ulist, 'university_rankings.csv')
