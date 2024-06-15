import time
import re
import urllib.request
import numpy as np
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def scanPage(url, driver, tillPage):
    driver.get(url)

    currentPage = 1
    tillPage = tillPage
    lastPage = int(driver.find_element(By.CLASS_NAME, 'pagination-paginationMeta').text.split(' ')[-1])

    if tillPage is None :
        tillPage = lastPage

    imageUrls = []
    for i in range(currentPage, tillPage):
        href_selectors = driver.find_elements(By.CSS_SELECTOR, "a")
        shirtUrl = re.compile(r'^https://www.myntra.com/tshirts/')
        href_urls = [href.get_attribute('href') for href in href_selectors if href.get_attribute('href') is not None and shirtUrl.match(href.get_attribute('href'))]
        imageUrls.extend(href_urls)

        clickNext = driver.find_element(By.CLASS_NAME, "pagination-next")
        ActionChains(driver)\
            .click(clickNext)\
            .perform()
        time.sleep(5)

    return imageUrls
