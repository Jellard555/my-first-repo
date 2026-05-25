import requests
from bs4 import BeautifulSoup
import re
import csv
url = "https://thetowerinfo.com/tallest-skyscrapers/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find("title").text
tower_name = soup.find_all("h2")[:20]
data = []
for i in tower_name:
    name = i.find("strong").text
    data.append(name)
'''print(data)'''
height = soup.find_all("span", attrs= {"style": "font-size: 14pt;"})[:120]
temp = []
for a in height:
    try:
        data_name, info = a.text.split(":")
        item = (data_name.strip(), info.strip())
        temp.append(item)
    except ValueError:
        a, b, c = a.text.split(":")
        item1 = (a, "2019")
        item2 = ("Location:", c)
        temp.append(item1)
        temp.append(item2)
groups = []
current_group = []

for item in temp:
    key = item[0]
    if key.startswith("Standard height"):
        if current_group:
            groups.append(current_group)
        current_group = [item]
    else:
        current_group.append(item)

if current_group:
    groups.append(current_group)
with open("data.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)

    for i, group in enumerate(groups, 1):
        row = [data[i-1]]
        for k, v in group:
            row.append(k)
            row.append(v)
        writer.writerow(row)

print(f"finish")
print("data.csv")
#print(temp)



content = soup.get_text()
#print("Title:", tower_name)
