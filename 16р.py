from bs4 import BeautifulSoup
import requests
response = requests.get("https://privatbank.ua/rates-archive")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("div", {"class":"purchase"})
    res = soup_list[1]
print(res.text)
grn=float(input("введіть суму гривень "))
kurs= float(res.text)
print("ви отримуете ",round(grn/kurs,2),"$")
