from scraper import scrape

male_urls = [
'https://www.myntra.com/men-casual-trousers',
]

female_urls = [
'https://www.myntra.com/myntra-fashion-store?f=Categories%3AClothing%20Set%2CCo-Ords%3A%3AGender%3Amen%20women%2Cwomen',
'https://www.myntra.com/playsuit?f=Gender%3Amen%20women%2Cwomen',
'https://www.myntra.com/jumpsuits?f=Gender%3Amen%20women%2Cwomen',
]

for i in range(0, len(male_urls)-1):
    file_name = male_urls[i].split('/')[-1]
    print(file_name)
    scrape(male_urls[i], file_name)

for i in range(0, len(female_urls)-1):
    file_name = female_urls[i].split('/')[-1]
    scrape(female_urls[i], file_name)

