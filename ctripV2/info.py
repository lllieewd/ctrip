# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from ctripV2.items import info_entity


def info(hotelId, checkIn, checkOut, cityId):
    response = requests.get(
        "https://hotels.ctrip.com/hotels/detail/?hotelId="+str(hotelId)+"&checkIn="+checkIn+"&checkOut="+checkOut+"&cityId="+str(cityId))
    soup = BeautifulSoup(response.text, features='html.parser')
    div = soup.find(name='div', attrs={"class": "detail-headtraffic_traffic"})
    li_list = div.find_all(name='li')

    flight_distance = ''
    train_distance = ''
    subway_distance = ''

    for li in li_list:
        i = li.find(name='i', attrs={"class": "detail-headtraffic_icon"})
        type = i.get('type')
        if type == 'flight':
            flight_distance = li.text
        if type == 'ic_new_bu_train':
            train_distance = li.text
        if type == 'ic_new_subway':
            subway_distance = li.text
    div1 = soup.find(name='div', attrs={"class": "detail-headtraffic_traffic_desc"})
    place_info = div1.text
    return info_entity(flight_distance, train_distance, subway_distance, place_info)
