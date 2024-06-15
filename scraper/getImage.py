import time
import os
import urllib.request
import uuid
import numpy as np
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By

def getImage(url, driver, saveTo):
    driver.get(url)

    imgObjs = driver.find_elements(By.CLASS_NAME, 'image-grid-image')
    imgStyle = [image.get_attribute('style') for image in imgObjs]
    imgUrls = [link.split('url("')[1][:-3] for link in imgStyle]
    sleeps = [1,0.5,1.5,0.7]

    saveTo = saveTo
    if saveTo is None:
        saveTo = 'gotImage'

    if not os.path.exists(saveTo):
        os.makedirs(saveTo)

    for i,link in enumerate(tqdm(imgUrls)):
        saveImg = os.path.join(saveTo, f'{saveTo}_{i}_{uuid.uuid4()}.jpeg')
        urllib.request.urlretrieve(link, saveImg)
        time.sleep(np.random.choice(sleeps))

