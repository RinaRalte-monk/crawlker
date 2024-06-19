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

def scrape(url, save_to):
    print("init function ran")
    driver = webdriver.Chrome()

    image_links = scan_page(url, driver)

    for i in range(0, len(image_links)-1):
        get_image(image_links[i], driver, save_to)

    driver.quit()


