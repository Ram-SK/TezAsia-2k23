import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def get_media(soup):
    media = []
    for img in soup.find_all('img'):
        media.append(img['src'])
    for video in soup.find_all('video'):
        media.append(video['src'])
    return media

def execute():
    url = 'https://unstop.com/'
    soup = scrape_webpage(url)
    media = get_media(soup)
    print(media)

if __name__ == '__main__':
    execute()