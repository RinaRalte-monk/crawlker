import time
import re
import urllib.request
import numpy as np
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from .nav import scan_page
from .getimage import get_image

def scrape(url, driver, save_to):
    print("scraping", url)
    driver = webdriver.Chrome()
    driver.get(url)

    scan_page(url, driver)

    driver.quit()


