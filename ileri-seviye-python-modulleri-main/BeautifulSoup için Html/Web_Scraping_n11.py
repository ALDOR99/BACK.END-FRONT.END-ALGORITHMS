import requests
from bs4 import BeautifulSoup


url = "https://www.n11.com/arama?q=laptop"


html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")


list = soup.find_all("li",{"class":"column"})
for li in list:
    name = li.div.a.text.strip()
    link = li.div.a.get("href")
    oldprice = li.a.find("div",{"class":"proDetail"}).find_all("a")[0].text.strip().strip("TL")
    newprice = li.a.find("div",{"class":"proDetail"}).find_all("a")[1].text.strip().strip("TL")


    print(f"name: {name} link:{link} old price:{oldprice} new price: {newprice}")



