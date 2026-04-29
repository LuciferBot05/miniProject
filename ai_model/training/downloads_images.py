import os
from icrawler.builtin import GoogleImageCrawler

def download(keyword, folder):
    crawler = GoogleImageCrawler(storage={'root_dir': folder})
    crawler.crawl(keyword=keyword, max_num=100)

download('battery waste', 'dataset/battery')
download('cable waste', 'dataset/cable')
download('circuit board waste', 'dataset/circuit_board')
download('mobile phone waste', 'dataset/mobile')
