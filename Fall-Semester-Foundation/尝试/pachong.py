import requests
#response = requests.get("http://books.toscrape.com/")
#if response.ok:
 #   print(response.text)
#else:
 #   print("请求失败")
response = requests.get("http://moive.douban.com/top250")
print(response.status_code)