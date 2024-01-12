@echo off
color 4
echo YOU NEED PYTHON 3.11.2 OR HIGH VERSION INSTALLED
echo Installing a Scrapy libs...
echo Made by pedrokakzzx
pip install scrapy
echo Successful installation...
scrapy crawl quotes
echo Successful
start getsite\saved_pages
pause