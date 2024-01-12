from pathlib import Path
from colorama import init, Fore

import colorama
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        print("English")
        print("ENTER A WEBSITE LINK BELOW")
        print("THE LINK MUST START WITH HTTPS://")  
        print("Português Brasileiro")
        print("DIGITE UM LINK DE UM SITE ABAIXO")
        print("O LINK PRECISA COMEÇAR COM HTTPS:// ")
        
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