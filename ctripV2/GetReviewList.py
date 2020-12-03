# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import json

import requests

from ctripV2 import cookie
from ctripV2.items import review_entity

def hotel_review(hotel_id, pvid):
    url = "https://m.ctrip.com/restapi/soa2/16709/json/GetReviewList"
    headers = {
        'authority': 'm.ctrip.com',
        'method': 'POST',
        'path': '/restapi/soa2/16709/json/GetReviewList',
        'scheme': 'https',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '547',
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

    payload = {"PageNo": 1, "PageSize": 10, "MasterHotelId": hotel_id, "NeedFilter": True, "UnUsefulPageNo": 1,
               "UnUsefulPageSize": 5, "isHasFold": False,
               "head": {"Locale": "zh-CN", "Currency": "CNY", "Device": "PC", "UserIP": cookie.getUserIp(), "Group": "",
                        "ReferenceID": "", "UserRegion": "CN", "AID": None, "SID": None, "Ticket": "", "UID": "",
                        "IsQuickBooking": "", "ClientID": cookie.getClientId(), "OUID": None, "TimeZone": "8",
                        "P": "61884674695", "PageID": "102003", "Version": "",
                        "HotelExtension": {"WebpSupport": True, "group": "CTRIP", "Qid": "133903662091",
                                           "hasAidInUrl": False},
                        "Frontend": {"vid": cookie.getClientId(), "sessionID": 6, "pvid": pvid}}, "ServerData": ""}

    r = requests.post(url, data=json.dumps(payload), headers=headers)  # formData,
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    json_data = json.loads(r.text)
    base_info = json_data['Response']['ReviewBaseInfo']
    score = dict(base_info).get('score')
    totalReviews = dict(base_info).get('totalReviews')
    keywords = []
    review_list = json_data['Response']['ReviewFilterList']
    for review in review_list:
        hotel_type = review['type']
        if hotel_type == 'tagTheme':
            keywords.append(review['name'])
    return review_entity(score, totalReviews, keywords)
