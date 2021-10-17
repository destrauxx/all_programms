import sys
import requests

from bs4 import BeautifulSoup

query = sys.argv[1] if len(sys.argv) > 1 else input('Тип аватара- ')

url = f'https:/www.kiddle.co/s.php?q={query}'

page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')