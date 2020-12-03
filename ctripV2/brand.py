# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from ctripV2.items import brand_entity


def brand(hotelId):
    response = requests.get("https://hotels.ctrip.com/hotel/" + str(hotelId) + ".html")
    soup = BeautifulSoup(response.text, features='html.parser')
    div = soup.find(name='div', attrs={"class": "grade"})
    span = div.find(name='span')
    hotel_title = span.get('title')
    div1 = div.find(name='div', attrs={"class": "special_label"})
    i_list = div1.find_all(name='i')
    brand = []
    for i in i_list:
        # print(i.get('class'))
        if i.get('class')[0] == 'i_label':
            brand.append(i.text)
    span1 = soup.find(name='span', attrs={"class": "htl_group_name"})
    group_name = ''
    if span1 is not None:
        group_name = span1.text
    return brand_entity(group_name, hotel_title, brand)

if __name__ == '__main__':
    brand_entity = brand('25680819')
    print(brand_entity.group_name)
    print(brand_entity.hotel_title)
    print(','.join(brand_entity.brand))
