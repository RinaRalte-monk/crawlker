import scraper

menUrl = 'https://www.myntra.com/men-tshirts'
womenUrl = 'https://www.myntra.com/men-tshirts'

manSaveTo = 't1'
womanSaveTo = 't2'
tillPage = 2

scraper.scrape(menUrl, manSaveTo, tillPage)
scraper.scrape(womenUrl, womanSaveTo, tillPage)

