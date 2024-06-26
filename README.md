# Crawler

A python script that scrape images

### 1.1 scraper Module  - __init__.py

init.py to intialize the folder as a module
scrape functions that takes two arguments:
    url: targeted url you want to scrape
    save_to : which folder you want to save the scraped images

```
def scrape(url, save_to):
    driver = webdriver.Chrome()
    driver.get(url)

    href_selectors = driver.find_elements(By.CSS_SELECTOR, "a")
    href_urls = [href.get_attribute('href') for href in href_selectors if href.get_attribute('href') is not None and href.get_attribute('href').endswith('/buy')]
    count = 0
    for href in href_urls :
        if count == 50:
            break
        folder_name = href.split("/")[-3]
        folder_path = os.path.join(save_to, folder_name)
        get_image(href,driver, folder_path)
        count = count + 1

    driver.quit()
```
creates a driver variable for the selenium webdriver
use the driver to load the desired (url)
```
driver = webdriver.Chrome()
driver.get(url)
```
href selectors selects elements by css selector every<a>
then stores every <a> that has a 'href' attributes inside the href_urls
```
href_selectors = driver.find_elements(By.CSS_SELECTOR, "a")
href_urls = [href.get_attribute('href') for href in href_selectors if href.get_attribute('href') is not None and href.get_attribute('href').endswith('/buy')]
```
counts upto 50 to download only 50 images
for each elements inside the href_urls scrapes
the images using the get_image() function
close driver
```
    count = 0
    for href in href_urls :
        if count == 50:
            break
        folder_name = href.split("/")[-3]
        folder_path = os.path.join(save_to, folder_name)
        get_image(href,driver, folder_path)
        count = count + 1

    driver.quit()
```

### 1.2 scraper Module - get_image.py


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
