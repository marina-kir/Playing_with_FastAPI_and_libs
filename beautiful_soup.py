from bs4 import BeautifulSoup
import requests

path = "https://www.ynet.co.il"
html_doc = requests.get(path)
soup = BeautifulSoup(html_doc.text, 'html.parser')
# print (html_doc.text)
# print ("-------------------------------------------------------------------")
# print(soup.prettify())

print (list(soup.descendants))