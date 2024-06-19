from scraper import scrape

male_urls = [
'https://www.myntra.com/men-tshirts',
'https://www.myntra.com/men-casual-shirts',
'https://www.myntra.com/men-formal-shirts',
]

female_urls = [
'https://www.myntra.com/women-kurtas-kurtis-suits',
'https://www.myntra.com/ethnic-tops',
'https://www.myntra.com/saree',
]

for i in range(0, len(male_urls)-1):
    file_name = male_urls[i].split('/')[-1]
    print(file_name)
    scrape(male_urls[i], file_name)

for i in range(0, len(female_urls)-1):
    file_name = female_urls[i].split('/')[-1]
    scrape(female_urls[i], file_name)

