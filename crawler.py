import time
import re
import urllib.request
import numpy as np
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from nav import scanPage
from getImage import getImage
from scrape import scrape

driver = webdriver.Chrome()

menUrl = 'https://www.myntra.com/men-tshirts'
womenUrl = 'https://www.myntra.com/men-tshirts'

womanSaveTo = 'womanShirts'
manSaveTo = 'menShirts'
tillPage = 3

scrape(menUrl, driver, manSaveTo, tillPage)
scrape(womenUrl, driver, womanSaveTo, tillPage)

driver.quit()
