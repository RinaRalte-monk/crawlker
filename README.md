# Crawler

A python script that scrape images

### 1.1 scraper Module  - __init__.py

- init.py to intialize the folder as a module
scrape functions that takes two arguments:
<br><space>url: targeted url you want to scrape
<br><space>save_to : which folder you want to save the scraped images

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


<br>

- creates a driver variable for the selenium webdriver
use the driver to load the desired (url)

```
driver = webdriver.Chrome()
driver.get(url)
```


<br>

- href selectors selects elements by css selector every<a>
then stores every <a> that has a 'href' attributes inside the href_urls

```
href_selectors = driver.find_elements(By.CSS_SELECTOR, "a")
href_urls = [href.get_attribute('href') for href in href_selectors if href.get_attribute('href') is not None and href.get_attribute('href').endswith('/buy')]
```



<br>

- counts upto 50 to download only 50 images
for each elements inside the href_urls scrapes
the images using the get_image() function

```
close driver
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

<br>

### 1.2 scraper Module - get_image.py

- the bread and butter of the code
<br> a method that will take three arguments :
<br><space>url : url of targeted page
<br><space>driver : selenium driver
<br><space>save_to : save image to desired folder

```
def get_image(url, driver, save_to)
    driver.get(url)

    img_objs = driver.find_elements(By.CLASS_NAME, 'image-grid-image')
    img_style = [image.get_attribute('style') for image in img_objs]
    img_urls = [link.split('url("')[1][:-3] for link in img_style]
    sleeps = [1,0.5,1.5,0.7]

    save_to = save_to
    if save_to is None:
        save_to = 'gotImage'

    save_path = os.path.join('Images', save_to)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for i,link in enumerate(tqdm(img_urls)):
        img_name = i.split['/'][-3]
        save_img = os.path.join(save_path, f'{img_name}.jpeg')
        urllib.request.urlretrieve(link, save_img)
        time.sleep(np.random.choice(sleeps))
```

<br>

- use driver to find imgaes through class ->
<br><space>filter it by attribute of 'style'
<br><space>clean the 'style' list to get proper urls

```
    img_objs = driver.find_elements(By.CLASS_NAME, 'image-grid-image')
    img_style = [image.get_attribute('style') for image in img_objs]
    img_urls = [link.split('url("')[1][:-3] for link in img_style]
```

- prepares the path for the downloaded images
<br><space>if save_to is not have a default folder
<br><space>if not None set the path under 'Images' folder

```
    save_to = save_to
    if save_to is None:
        save_to = 'gotImage'

    save_path = os.path.join('Images', save_to)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
```

<br>

- looping through the img_urls
<br><space>use the part of the url name as folder name
<br><space>using urllib to retrieve the img
<br><space>give it random sleep to make it seem human not get blocked

```
    for i,link in enumerate(tqdm(img_urls)):
        img_name = i.split['/'][-3]
        save_img = os.path.join(save_path, f'{img_name}.jpeg')
        urllib.request.urlretrieve(link, save_img)
        time.sleep(np.random.choice(sleeps))
```

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
