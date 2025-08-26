'''
Real-World Exampe: Multithreading for I/O bound tasks
Scenario: Web Scrapping
Web Scrapping often involves making numerous network requess to fetch web pages. These taks are I/O-bound 
because they spend a lot of time waiting for responses from servers. Multithreading can significantly
improve the performance by allowning multiple web pages to be fetched concurrently
'''

import threading
import requests
from bs4 import BeautifulSoup


urls=[
    'https://python.langchain.com/docs/tutorials/',
    'https://python.langchain.com/docs/how_to/pydantic_compatibility/',
    'https://python.langchain.com/docs/versions/migrating_memory/'
]

def fetch_content(url):
    response = requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched{len(soup.text)} character from {url}')
    
threads=[]

for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    print('All web pages fetched')