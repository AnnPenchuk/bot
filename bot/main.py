
import telebot


import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import datetime


token = '6255337724:AAHiboJTGXmN52j7ugIqIzF3RvmYcIL8umY'  # <<< токен

bot = telebot.TeleBot(token)


def get_html(url, priceTo, priceFrom, arrival, departure, maleCount):
    html = url + '?o%5BpriceTo%5D=' + priceTo + '&o%5BpriceFrom%5D=' + priceFrom + '&o%5Barrival%5D=' + arrival + '&o%5Bdeparture%5D=' + departure + '&o%5BmaleCount%5D=' + maleCount
    print(html)
    return html

@bot.message_handler(commands=['start'])
def say_hi(message):
    bot.send_message(message.chat.id, 'Привет, '+message.chat.first_name+" "+message.chat.last_name)
    sent_msg=bot.send_message(message.chat.id, 'Введите день заезда (в формате 28.08.23):')
    bot.register_next_step_handler(sent_msg,data)



@bot.message_handler(content_types=["text"])
def data(pm):
    date_string1 = pm.text
    sent_msg = bot.send_message(pm.chat.id, "Введите день выезда (в формате 29.08.23):")
    bot.register_next_step_handler(sent_msg, price1)  # Next message will call t
    print(date_string1)
    return date_string1


def price1(pm):
    date_string2 = pm.text
    print(date_string2)
    sent_msg= bot.send_message(pm.chat.id, 'Введите минимальную стоимость за сутки: ')
    bot.register_next_step_handler(sent_msg, price2)
    return date_string2

def price2(pm):
    priceFrom = pm.text
    print(priceFrom)
    sent_msg= bot.send_message(pm.chat.id, 'Введите максимальную стоимость за сутки: ')
    bot.register_next_step_handler(sent_msg, count)
    return priceFrom


def count(pm):
    priceTo=pm.text
    sent_msg=bot.send_message(pm.chat.id, 'Введите количество гостей:  ')
    bot.register_next_step_handler(sent_msg, end)
    print(priceTo)
    return priceTo


def end(pm):
    maleCount = pm.text
    print(maleCount)
    sent_msg =bot.send_message(pm.chat.id, 'Сейчас подберу квартиры')
    bot.register_next_step_handler(sent_msg, parsing)
    return maleCount


def parsing(date_string1,date_string2,priceFrom,priceTo,maleCount):
    url='https://tvil.ru/city/rostov-na-donu/flats/'

    #date_string1= input('Введите день заезда (в формате 28.08.23): ')
    arrival =datetime.datetime.strptime(date_string1, '%d.%m.%y').date()
    print(arrival)
   # date_string2 = input('Введите день выезда (в формате 29.08.23): ')
    departure=datetime.datetime.strptime(date_string2, '%d.%m.%y').date()
    print(departure)
    #print(arrival,departure)
    delta = departure - arrival
    departure=str(departure)
    arrival=str(arrival)
    print(delta.days)
    #priceFrom = input('Введите минимальную стоимость за сутки: ')
   # priceTo = input('Введите максимальную стоимость за сутки: ')
    delta=int(delta.days)
    priceTo=str(delta*int(priceTo))
    #print(priceTo)
   #maleCount=input('Введите количество гостей: ')

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

    return abs_url


bot.polling()

