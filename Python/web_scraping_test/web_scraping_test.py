from bs4 import BeautifulSoup
import requests

url = "https://thotcomputacion.com.uy/categoria-producto/equipos-armados/"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

""" print(doc.prettify()) """

prices = doc.find_all(string="US$")

parent = prices[0].parent

print(parent.string)