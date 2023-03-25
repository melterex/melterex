import requests
import time
from bs4 import BeautifulSoup
name = input()
url = f"https://codeforces.com/api/user.status?handle={name}&from=1&count=10"
r = requests.get(url)
soup = BeautifulSoup(r.text)
soup.count("problem")
time.sleep(5)