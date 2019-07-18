import requests as r 
from bs4 import BeautifulSoup as bs
import time
from tqdm import tqdm
import sqlite3


headers = {"accept":"*/*" ,"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
base_url = 'https://hh.ru/search/vacancy?search_period=30&clusters=true&area=1&text=Python&enable_snippets=true'



session = r.Session()
request = session.get(base_url, headers=headers)
if request.status_code == 200: 
    print("It's ok!")








    soup = bs(request.content, "html.parser")
    divs = soup.find_all("div", attrs= {"data-qa":"vacancy-serp__vacancy"})
    for div in divs:
        title = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-title'}).text
        href = div.find('a',attrs = {'data-qa':'vacancy-serp__vacancy-title'})['href']
        company = div.find('a', attrs = {'data-qa':'vacancy-serp__vacancy-employer'}).text
        #print(title,href,company)

else:
    print("Error!")