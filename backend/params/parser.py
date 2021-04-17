import requests
from bs4 import BeautifulSoup as BS
from itertools import count

from .models import DirectionModel


def parse(): 
    data = BS(requests.get('http://unpo.tomsk.gov.ru/Institutions/SPO').text)
    colledges = [i.find('h3').text for i in data.find_all('a', {'class': 'item-header expandable-button'})]

    counter = dict()
    for i in count(1):
        r = requests.get(f'http://unpo.tomsk.gov.ru/Institutions/Details/{i}')
        if r.status_code == 200:
            bs = BS(r.text)
            name = bs.find('h2').text

            content = bs.find('div', {'class':'content-container'})
            titles = [i.text for i in content.find_all('div', {'class':'qr-spoiler-caption'})]

            try:
                table = content.find_all('table')[titles.index('Специальности')]
            except Exception: continue
            specs = [i.find('td').text.strip().replace('\xa0', '') for i in table.find_all('tr')][1:]

            try:
                table = content.find_all('table')[titles.index('Профессии')]
            except Exception: continue
            prof = [i.find('td').text.strip().replace('\xa0', '') for i in table.find_all('tr')][1:]

            counter[name] = {
                'specs': specs,
                'prof': prof
            }
        
        if len(counter.items()) == len(colledges): break
        if i > 50: break
    return counter

def save_parse(data):
    for colledge_name, data in data.items():
        for direction in data.get('specs'):
            if direction:
                DirectionModel(spec_name=direction, colledge_name=colledge_name).save()
        for direction in data.get('prof'):
            if direction:
                DirectionModel(prof_name=direction, colledge_name=colledge_name).save()
