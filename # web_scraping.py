# web_scraping
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")
    paragraphs = soup.find_all("p")
    full_text = "\n".join([p.get_text() for p in paragraphs])
    print("✅ :", len(full_text))
    print(full_text[:])
else:

    print("⚠️ :", response.status_code)
