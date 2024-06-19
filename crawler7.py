from scraper import scrape

male_urls = [
]

female_urls = [
'https://www.myntra.com/women-blazers-waistcoats',
'https://www.myntra.com/women-loungewear-and-nightwear',
'https://www.myntra.com/women-swimwear',
]

for i in range(0, len(male_urls)-1):
    file_name = male_urls[i].split('/')[-1]
    print(file_name)
    scrape(male_urls[i], file_name)

for i in range(0, len(female_urls)-1):
    file_name = female_urls[i].split('/')[-1]
    scrape(female_urls[i], file_name)

