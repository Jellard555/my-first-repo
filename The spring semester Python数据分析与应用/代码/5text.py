from pyecharts.globals import CurrentConfig, OnlineHostType
CurrentConfig.ONLINE_HOST = "https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/"
import pandas as pd
from pyecharts.charts import Bar
from pyecharts.charts import Map
from pyecharts.charts import Pie
from pyecharts import options as opts
import webbrowser
import os
import subprocess
df_school = pd.read_csv('university_rankings.csv',encoding="utf-8")
df_school_count = df_school.groupby("省市")  # 按“省市”分组
df_school_count = df_school_count.size()  # 统计每组数量
df_school_count = df_school_count.reset_index()  # 转成正常表格
df_school_count.columns = ["省份", "学校数量"]  # 重命名列名
print(df_school_count.head())
print(df_school_count.columns.tolist())
province_fix = {
    "北京省": "北京",
    "上海市": "上海",
    "广西": "广西壮族自治区",
    "内蒙": "内蒙古自治区",
    "西藏": "西藏自治区",
    "宁夏": "宁夏回族自治区",
    "新疆": "新疆维吾尔自治区",
    "香港": "香港特别行政区",
    "澳门": "澳门特别行政区"
}
df_school_count['省份'] = df_school_count['省份'].replace(province_fix)


m1 =(Map(init_opts=opts.InitOpts(theme='dark', width='1000px', height='600px', bg_color='#0d0735')))
m1.add('学校数量',
data_pair = [list(z) for z in zip(df_school_count['省份'].tolist(), df_school_count['学校数量'].tolist())],
             maptype='china',
             zoom=1,
             is_map_symbol_show=True,# 显示地图符号
             label_opts=opts.LabelOpts(is_show=True, color='white'),# 显示标签，字体颜色为黑色
             itemstyle_opts=opts.ItemStyleOpts(
                 border_color='#fff',# 行政区划线颜色
                 border_width=1# 行政区划线宽度
)
)
m1.set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                min_=df_school_count["学校数量"].min(),
                max_=df_school_count["学校数量"].max(),
                is_piecewise=False,
                type_="color",
                #series_index=0,
                pos_top='60%',
                pos_left='10%',
# 使用默认的颜色范围
                range_color=None
),
            tooltip_opts=opts.TooltipOpts(formatter='{b}:{c}所'),
            title_opts=opts.TitleOpts(
                title='2026全国高校分布地图',
                pos_top='2%',
                pos_left="2%",
                title_textstyle_opts=opts.TextStyleOpts(color='#fff200', font_size=20)
)
)
m1.render()
file_path = os.path.abspath("render.html")
print(f"succeed!")
webbrowser.open(f"file://{file_path}")
