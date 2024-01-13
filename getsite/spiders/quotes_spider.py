from pathlib import Path
from colorama import init, Fore

import colorama
import scrapy
import os


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        os.system("cls")
        os.system("clear")        
        print("Enter a website link bellow:")
        
        link = input("Link:")
        urls = [
            link
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        save_folder = Path("getsite\saved_pages")
        save_folder.mkdir(parents=True, exist_ok=True)
        filename = save_folder / f"page-{response.url.split('/')[-1]}.html"
        filename.write_bytes(response.body)
        self.log(f"Saved file {filename}")
