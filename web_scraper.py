import requests
from bs4 import BeautifulSoup

def scrape_web(url):
   
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def execute_scraper(urls):

    for url in urls:
        data = scrape_web(url)
        print(data)

if __name__ == '__main__':
    urls = ['https://www.flipkart.com']
    execute_scraper(urls)