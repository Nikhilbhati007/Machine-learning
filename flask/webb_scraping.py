import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.cricbuzz.com/")
print(res)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
print(soup.title.get_text(strip=True) if soup.title else "No title found")

