import requests
from bs4 import BeautifulSoup
import webbrowser
def getHTMLText(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    demo = r.text
    with open("my_web.html",'w',encoding="utf-8") as f:
        f.write(demo)
    webbrowser.open("my_web.html")
    soup = BeautifulSoup(demo,"html.parser")
    print(soup.prettify())
a= getHTMLText("https://nba.hupu.com/games/boxscore/168791")