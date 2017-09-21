
import scrapy
from meiplay.items import DramaItem
from bs4 import BeautifulSoup
from database.database import Database

class FenglinSpider(scrapy.spiders.Spider):
    name = "fenglin"
    allowed_domains = ["maplestage.com"]
    base_url = "http://maplestage.com"
    zones = {
        "http://maplestage.com/drama/cn" : {
            'en_name' : 'CN Drama',
            'cn_name' : '大陸戲劇'
        }
    }
    start_urls = [
        "http://maplestage.com/drama/cn"
    ]
    
    def start_request(self):  

    def parse_recommed(self, response):
        recommend_dramas = BeautifulSoup(response.text, 'lxml').find_all('a', class_ = "shows-row-module__item___2HLRl");
        for recommend_drama in recommend_dramas:
            drama_item = DramaItem()
            drama_item['link'] = base_url + recommend_drama['href'].strip()
            drama_item['fenglin_name'] = recommend_drama.find('div')[0]['style']



    def parse_home_page(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

    def parse_category(self, response):
        pass

    def parse_zone(self, response):
        pass

    def parse_drama(self, response):
        pass
