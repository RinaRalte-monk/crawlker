from scraper import scrape

male_urls = [
'https://www.myntra.com/men-blazers',
'https://www.myntra.com/men-suits',
'https://www.myntra.com/rain-jacket',
]

female_urls = [
'https://www.myntra.com/lehenga-choli',
'https://www.myntra.com/dupatta-shawl',
'https://www.myntra.com/women-jackets', ]

for i in range(0, len(male_urls)-1):
    file_name = male_urls[i].split('/')[-1]
    print(file_name)
    scrape(male_urls[i], file_name)

for i in range(0, len(female_urls)-1):
    file_name = female_urls[i].split('/')[-1]
    scrape(female_urls[i], file_name)

