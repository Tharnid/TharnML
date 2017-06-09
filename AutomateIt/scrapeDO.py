from lxml import html
import requests

page = requests.get('https://github.com/pricing/')
tree = html.fromstring(page.content)
print("Page Object:", tree)
pricing = tree.xpath('//span[@class="default-currency"]/text()')
print("nPricing:", pricing)
