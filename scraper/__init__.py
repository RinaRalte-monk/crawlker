import time
import re
import urllib.request
import numpy as np
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from .nav import scanPage
from .getImage import getImage

def scrape(url, saveTo, tillPage):
    driver = webdriver.Chrome()

    imageLinks = scanPage(url, driver, tillPage)

    for i in range(0, len(imageLinks)-1):
        getImage(imageLinks[i], driver, saveTo)

    driver.quit()


