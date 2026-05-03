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
df_top30 = df_school[:30]
df_top30 = df_top30.sort_values(by='总分', ascending=True)
# 定义绘制柱状图的函数


bar = Bar(init_opts=opts.InitOpts(theme='dark', bg_color='#0d0735',height = "1400px"))# 设置背景颜色为深蓝色
bar.add_xaxis(df_top30['中文名'].tolist())# 将中文名作为横坐标
bar.add_yaxis('', df_top30['总分'].tolist())# 分数作为纵坐标
bar.reversal_axis()# 交换 x 和 y 轴
bar.set_global_opts(
            title_opts=opts.TitleOpts(
                title='2026中国大学综合排名TOP30',
                pos_top='1%',
                pos_left="0.5%",
                title_textstyle_opts=opts.TextStyleOpts(color='#FFFFFF')# 设置标题字体颜色为白色
),
            visualmap_opts=opts.VisualMapOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(color='#FFFFFF')),# 设置x轴标签颜色为白色
            #yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(color='#FFFFFF'))# 设置y轴标签颜色为白色
#)
            yaxis_opts=opts.AxisOpts(
    axislabel_opts=opts.LabelOpts(
        color='white',
        # 核心：设置标签字体大小
        text_style_opts=opts.TextStyleOpts(font_size=9)
    )
))

bar.render()
file_path = os.path.abspath("render.html")
print(f"succeed!")
os.startfile(file_path)