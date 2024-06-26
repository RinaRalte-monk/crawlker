# Crawler

A python script that scrape images

### 1.1 Scrape Module

### 2.1 crawler_main.py👍

Imports scrape from the scraper module ( explained below )
```
import os
from scraper import scrape
```
Male_urls, female_urls : a list that holds the numerous urls
```
male_urls = [
    lists of urls here
]

female_urls = [
    lists of urls here
]
```
Loops through the list
Stores the the last part of the /url in file_name
Creates file path men/file_name for the scrape()
Call scrape()
print() to know which ones are done downloading
```
for i in range(0, len(male_urls)):
    file_name = male_urls[i].split('/')[-1]
    file_path = os.path.join('men', file_name)
    scrape(male_urls[i], file_path)
    print("Saved at :", file_path)

for i in range(0, len(female_urls)):
    file_name = female_urls[i].split('/')[-1]
    file_no = str(i)
    file_path = os.path.join('women', file_name, file_no)
    scrape(male_urls[i], file_path)
    print("Saved at:", file_path)
```
