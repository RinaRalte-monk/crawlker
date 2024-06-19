from scraper import scrape

male_urls = [
'https://www.myntra.com/men-formal-trousers',
'https://www.myntra.com/mens-shorts',
'https://www.myntra.com/men-trackpants',
]

female_urls = [
'https://www.myntra.com/women-shrugs',
'https://www.myntra.com/women-sweaters-sweatshirts',
'https://www.myntra.com/women-jackets-coats',
]

for i in range(0, len(male_urls)-1):
    file_name = male_urls[i].split('/')[-1]
    print(file_name)
    scrape(male_urls[i], file_name)

for i in range(0, len(female_urls)-1):
    file_name = female_urls[i].split('/')[-1]
    scrape(female_urls[i], file_name)

