from nav import scanPage
from getImage import getImage

def scrape(url, driver, saveTo, tillPage):
    imageLinks = scanPage(url, driver, tillPage)

    for i in range(0, len(imageLinks)-1):
        getImage(imageLinks[i], driver, saveTo)


