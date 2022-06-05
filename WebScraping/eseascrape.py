import requests
from bs4 import BeautifulSoup as bs

esea_user = input("Input ESEA User: ")
url = "https://play.esea.net/" + esea_user
r = requests.get(url)
soup = bs(r.content, "html.parser")

profile_image = soup.find("img", {"alt": "parkerg"})["src"]

print(profile_image)
