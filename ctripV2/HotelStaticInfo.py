# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import json

import requests

from ctripV2 import cookie
from ctripV2.items import static_entity


def static(hotelId, cityId, pvid):
    url = "https://m.ctrip.com/restapi/soa2/16709/json/hotelStaticInfo"
    headers = {
        'authority': 'm.ctrip.com',
        'method': 'POST',
        'path': 'https://m.ctrip.com/restapi/soa2/16709/json/hotelStaticInfo',
        'scheme': 'https',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '551',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': cookie.getCookie(),
        'origin': 'https://hotels.ctrip.com',
        'p': '61884674695',
        'pragma': 'no-cache',
        'referer': 'https://hotels.ctrip.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }

    payload = dict(masterHotelId=hotelId, isBusiness=False, feature=[], cityCode=cityId,
                   head={"Locale": "zh-CN", "Currency": "CNY", "Device": "PC", "UserIP": cookie.getUserIp(),
                         "Group": "",
                         "ReferenceID": "", "UserRegion": "CN", "AID": None, "SID": None, "Ticket": "", "UID": "",
                         "IsQuickBooking": "", "ClientID": cookie.getClientId(), "OUID": None, "TimeZone": "8",
                         "P": "61884674695", "PageID": "102003", "Version": "",
                         "HotelExtension": {"WebpSupport": True, "group": "CTRIP", "Qid": "472663081754",
                                            "hasAidInUrl": False},
                         "Frontend": {"vid": cookie.getClientId(), "sessionID": 5, "pvid": pvid}}, ServerData="")

    r = requests.post(url, data=json.dumps(payload), headers=headers)  # formData,
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    json_data = json.loads(r.text)
    # openDate, renovationDate, roomNum, hasDining, hasParking, hasWifi, hasPlane
    openDate = None
    renovationDate = None
    roomNum = None
    hasWifi = '否'
    hasPlane = '否'
    hasDining = '否'
    hotel_info = json_data['Response']['hotelInfo']
    for i in hotel_info['basic']['label']:
        if str(i).startswith('开业'):
            openDate = i
        elif str(i).startswith('装修'):
            renovationDate = i
        elif str(i).startswith('客房'):
            roomNum = i
    description = dict(hotel_info['basic']).get('description')
    hotel_policy = json_data['Response']['hotelPolicy']
    if dict(hotel_policy).get('dining') is not None:
        if hotel_policy['dining']['isProvide']:
            hasDining = '是'
    else:
        hasDining = '否'
    if dict(hotel_policy).get('parking') is not None:
        parkContent = dict(hotel_policy).get('parking')['content']
        if list(parkContent).__len__() == 0 or '不设停车场' in parkContent[0]:
            hasParking = '否'
        else:
            hasParking = '是'
    else:
        hasParking = '否'
    hotel_facility = dict(json_data['Response']).get('hotelFacility')
    if hotel_facility is not None:
        for facility in hotel_facility:
            if facility['title'] == '网络':
                if list(facility['content']).__len__() > 0:
                    hasWifi = '是'
            if facility['title'] == '交通服务':
                if list(facility['content']).__len__() > 0:
                    for i in facility['content']:
                        if i['facilityDesc'] == '接机服务':
                            hasPlane = '是'
    return static_entity(openDate, renovationDate, roomNum, hasDining, hasParking, hasWifi, hasPlane, description)
