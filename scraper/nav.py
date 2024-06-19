import time
import re
import urllib.request
import numpy as np
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def scan_page(url, driver):
    driver.get(url)

    #current_page = 1
    #till_page = till_page
    #last_page = int(driver.find_element(By.CLASS_NAME, 'pagination-paginationMeta').text.split(' ')[-1])

    #if till_page is None :
    #    till_page = last_page

    image_urls = []
    #for i in range(current_page, till_page):
    href_selectors = driver.find_elements(By.CSS_SELECTOR, "a")
    href_urls = [href.get_attribute('href') for href in href_selectors if href.get_attribute('href') is not None and href.get_attribute('href').endswith('/buy')]
    image_urls.extend(href_urls)

        #click_next = driver.find_element(By.CLASS_NAME, "pagination-next")
        #ActionChains(driver)\
        #    .click(click_next)\
        #    .perform()
        #time.sleep(5)
    image_urls = image_urls[:10]
    return image_urls
