from scraper import scrape

male_urls = [
'https://www.myntra.com/men-jackets',
]

female_urls = [
'https://www.myntra.com/women-ethnic-wear',
'https://www.myntra.com/women-ethnic-bottomwear?f=categories%3AChuridar%2CLeggings%2CSalwar',
'https://www.myntra.com/skirts-palazzos',
]

for i in range(0, len(male_urls)-1):
    file_name = male_urls[i].split('/')[-1]
    print(file_name)
    scrape(male_urls[i], file_name)

for i in range(0, len(female_urls)-1):
    file_name = female_urls[i].split('/')[-1]
    scrape(female_urls[i], file_name)

