
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import datetime


def get_html(url, priceTo, priceFrom, arrival, departure, maleCount):
    #html = requests.get(url)
    html = url+'?o%5BpriceTo%5D='+priceTo+'&o%5BpriceFrom%5D='+priceFrom+'&o%5Barrival%5D='+arrival+'&o%5Bdeparture%5D='+departure+'&o%5BmaleCount%5D='+maleCount
    print(html)
    return html

url='https://tvil.ru/city/rostov-na-donu/flats/'

'''
response = requests.get(url)
print(response.status_code)
priceTo='4000'
priceFrom='3000'
arrival='2023-08-28'
departure='2023-08-29'
maleCount='1'
'''
date_string1= input('Введите день заезда (в формате 28.08.23): ')
arrival =datetime.datetime.strptime(date_string1, '%d.%m.%y').date()
date_string2 = input('Введите день выезда (в формате 29.08.23): ')
departure=datetime.datetime.strptime(date_string2, '%d.%m.%y').date()
#print(arrival,departure)
delta = departure - arrival
departure=str(departure)
arrival=str(arrival)
#print(delta.days)
priceFrom = input('Введите минимальную стоимость за сутки: ')
priceTo = input('Введите максимальную стоимость за сутки: ')
delta=int(delta.days)
priceTo=str(delta*int(priceTo))
#print(priceTo)
maleCount=input('Введите количество гостей: ')


'''
arrival= input('Введите день заезда (в формате 2023-08-28): ')

departure = input('Введите день выезда (в формате 2023-08-29): ')

#print(arrival,departure)
#delta = departure - arrival
#departure=str(departure)
#arrival=str(arrival)
#print(delta.days)
priceFrom = input('Введите минимальную стоимость за сутки: ')
priceTo = input('Введите максимальную стоимость за сутки: ')

#delta=int(delta.days)
#priceTo=str(delta*int(priceTo))
#print(priceTo)
maleCount=input('Введите количество гостей: ')

'''
html=get_html(url, priceTo, priceFrom, arrival, departure, maleCount)
web_page = requests.get(html)
soup = BeautifulSoup(web_page.text, 'html.parser')


relative_url = soup.find(class_="title").attrs['href']

abs_url = 'https://tvil.ru'+relative_url
print(abs_url)


work_book = Workbook()
work_sheet=work_book.active

items = soup.find_all(class_='search-result-item')

for elem in items:
    title = elem.find(class_="title").text
    relative_url = elem.find(class_="title").attrs['href']
    url = 'https://tvil.ru' + relative_url
    row = [title, url]
    print(row)
    work_sheet.append(row)
work_book.save('квартиры.xlsx')






