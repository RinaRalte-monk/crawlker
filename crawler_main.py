import os
from scraper import scrape

urls = [
    #url lists here
]

for i in range(0, len(urls)):
    file_name = urls[i].split('/')[-1]
    file_path = os.path.join('men', file_name)
    scrape(urls[i], file_path)
    print("Saved at :", file_path)

