import requests
from bs4 import BeautifulSoup
import json

class CrawlData:
    __url =  "https://vuighe.net/anime/kinh-di"
    def __init__(self):
        self.soup = BeautifulSoup(requests.get(self.__url).text, features = "html.parser")
    def __str__(self):
        return self.soup.prettify()
    def get_all_data(self):
        alldata = []
        items = self.soup.find_all(class_ = "tray-item")
        for item in items:
            alldata.append({
                "url" : ''.join(['https://vuighe.net/',item.find('a').get('href')]),
                "img" : item.find('img').get('src'),
                "description": {
                    "title" : item.find(class_ = "tray-item-title").text,
                    "views" : item.find(class_ = "tray-film-views").text,
                    "genres" : item.find(class_ = "tray-film-genres").text,
                    "updata" : item.find(class_ = "tray-film-update").text
                }
            })
        return alldata
    def save_to_file(self, file):
        data = self.get_all_data()
        with open(''.join([file, '.json']), 'w', encoding = 'utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

               
crawl = CrawlData()
crawl.save_to_file('anime')