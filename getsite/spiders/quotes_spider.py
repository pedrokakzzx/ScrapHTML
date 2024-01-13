from pathlib import Path
import scrapy
import os

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        print("Enter a website link below:")
        link = input("Link:")
        urls = [link]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        user_directory = str(Path.home())

        save_folder = Path(user_directory) / "ScrapHTML" / "saved_pages"
        save_folder.mkdir(parents=True, exist_ok=True)

        filename = save_folder / f"page-{response.url.split('/')[-1]}.html"
        
        filename.write_bytes(response.body)

        self.log(f"Saved file {filename}")
