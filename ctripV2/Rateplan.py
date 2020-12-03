# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import json
import uuid

import requests
from ctripV2 import cookie
from ctripV2.items import room_entity

uid = str(uuid.uuid4())
suid = ''.join(uid.split('-'))


def room(hotelId, cityId, checkIn, checkOut, pvid):
    url = "https://m.ctrip.com/restapi/soa2/16709/json/rateplan?testab=" + suid
    # headers = {
    #     'authority': 'm.ctrip.com',
    #     'method': 'POST',
    #     'path': '/restapi/soa2/16709/json/rateplan?testab=' + suid,
    #     'scheme': 'https',
    #     'accept': 'application/json',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'zh-CN,zh;q=0.9',
    #     'cache-control': 'no-cache',
    #     'content-length': '1494',
    #     'content-type': 'application/json;charset=UTF-8',
    #     'cookie': cookie.getCookie(),
    #     'origin': 'https://hotels.ctrip.com',
    #     'p': '61884674695',
    #     'pragma': 'no-cache',
    #     'referer': 'https://hotels.ctrip.com/',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'cors',
    #     'sec-fetch-site': 'same-site',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    # }

    headers = {
        'authority': 'm.ctrip.com',
        'method': 'POST',
        'path': '/restapi/soa2/16709/json/rateplan?testab=04642f7d49deb94202b63219f043126ef05f07311b9f52a8eddd74e39aec33e7',
        'scheme': 'https',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '1495',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': '_abtest_userid=997c988c-7e80-4cb4-b840-d08bdc8709b6; _ga=GA1.2.1973624881.1573724682; _RSG=JEav0NQG1.5Fq5ytGT8NbB; _RDG=2830c1f470342329b6292bc1632e179328; _RGUID=5f8141a5-c0e6-4393-b957-21d437f05d0f; MKT_CKID=1579673323829.cwan2.87f3; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; _gid=GA1.2.1885360935.1604299135; MKT_CKID_LMT=1604299138779; MKT_Pagesource=PC; _RF1=119.130.106.158; intl_ht1=h4=112_8056970,1_608516,28_470094,1_6410223; _uetsid=1c73a5801cd611eb95f13d49e7263f47; _uetvid=1c73e2f01cd611eb8a99af0b95a5e265; _bfi=p1%3D102003%26p2%3D102003%26v1%3D81%26v2%3D80; __zpspc=9.6.1604366380.1604372534.26%231%7Cbaiduppc%7Cbaidu%7Cpp%7C%25E6%259C%25BA%25E7%25A5%25A8%7C%23; _jzqco=%7C%7C%7C%7C1604299138919%7C1.1752613493.1573724681772.1604372398992.1604372534742.1604372398992.1604372534742.undefined.0.0.74.74; appFloatCnt=65; _bfa=1.1573724678415.2ku552.1.1604308563626.1604366372011.6.82; _bfs=1.27',
        'origin': 'https://hotels.ctrip.com',
        'p': '61884674695',
        'pragma': 'no-cache',
        'referer': 'https://hotels.ctrip.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }

    payload = {"checkIn": checkIn, "checkOut": checkOut, "priceType": "", "adult": 1,
               "popularFacilityType": "", "mpRoom": "", "fgt": "", "hotelUniqueKey": "", "child": 0, "roomNum": 1,
               "masterHotelId": hotelId, "age": "", "cityId": cityId, "roomkey": "", "minCurr": "", "minPrice": "",
               "hotel": "hotelId",
               "ctripTrace": {"listRoomId": 469553887, "listShadowId": 0, "listPrice_cx": "597", "exchange": "1.0",
                              "currency": "RMB", "maskDifAvgCnyPrice": "0"}, "filterCondition": {}, "genk": True,
               "genKeyParam": {"a": hotelId, "b": checkIn, "c": checkOut, "d": "zh-cn", "e": 2},
               "head": {"Locale": "zh-CN", "Currency": "CNY", "Device": "PC", "UserIP": cookie.getUserIp(), "Group": "",
                        "ReferenceID": "", "UserRegion": "CN", "AID": None, "SID": None, "Ticket": "", "UID": "",
                        "IsQuickBooking": "", "ClientID": cookie.getClientId(), "OUID": None, "TimeZone": "8",
                        "P": "61884674695", "PageID": "102003", "Version": "",
                        "HotelExtension": {"WebpSupport": True, "group": "CTRIP", "Qid": "133903662091",
                                           "hasAidInUrl": False,
                                           "hotelUuidKey": "s8HysTKkheoFEGQWnYf8Y6ZEkYXMeZsEqXjUbWpYFNrc7e0XJ8Dx8YdUjt0w4fK5bj5YODx1kyobvnkjnY7bWlBYNtyfFj37WdheBmwzkj3cv3YfzvFDE1pY9neXMjDUe97wPfYPYFYGcv8metsYgsiLOYFYDYU3InsWnYthYGgiQ9iZoib7jbYsDEdUvcFYmAwnUY84JTXYkNwkY3HRpmwoUWN0EcnizFw8Lv5lwbLiTZyMGyFnWOLimYhdE7MxL8Rk6RnzvGgYFtj4BysSiQtv5ZYmsj9kj0oiLDy1pioYSAR1nJBGy9Uizby7BY0AEsHw7hyXtjGsEmkR1aJlYa4jB5wObvtbjtYBzYb0Jncw1HWl8e6ZRmAWGPjb4WZYhNYXkJ8Fw0oW8nenZRfNW03E4tWAYBNROUwhtW61EbHinmwfMvgOJa6jBMJD7wnsw6H",
                                           "hotelUuid": "4gO1unGdofn8VQU3"},
                        "Frontend": {"vid": cookie.getClientId(), "sessionID": 6, "pvid": pvid}}, "ServerData": ""}

    r = requests.post(url, data=json.dumps(payload), headers=headers)  # formData,
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    json_data = json.loads(r.text)
    print(json_data)
    # name, area, bed, floor, hasDinning, hasWindows, price
    result = []
    room_list = json_data['Response']['baseRooms']
    for roomItem in room_list:
        roomDict = dict(roomItem)
        baseRoom = roomDict.get('baseRoom')
        roomFloor = dict(baseRoom).get('roomFloor')
        roomName = dict(baseRoom).get('roomName')
        tempRoom = dict(baseRoom).get('roomSize')
        baseRoomId = dict(baseRoom).get('roomId')
        if tempRoom is not None:
            roomSize = dict(tempRoom).get('text')
        else:
            roomSize = ''

        saleRoom = roomDict.get('saleRoom')
        if saleRoom is None:
            continue
        for sale in saleRoom:
            sale = dict(sale)
            roomId = sale.get('base')['roomId']
            bed = []
            bedList = sale.get('bed')['contentListHover']
            for bedItem in bedList:
                bed.append(bedItem)
            bedType = []
            bedTypeList = sale.get('bed')['contentList']
            for bedTypeItem in bedTypeList:
                bedType.append(bedTypeItem)
            payType = sale.get('money')['payType']
            facility = sale.get('facility')
            hasDinning = '无餐食'
            hasWindows = '无窗'
            for i in facility:
                if i['type'] == 'MultiMeal':
                    hasDinning = i['content']
                if i['type'] == 'Window':
                    hasWindows = i['content']
            promotionList = sale.get('promotion')
            promotion = []
            for p in promotionList:
                if dict(p).get('hover') is not None:
                    promotion.append(p['hover'])
            policyList = sale.get('policy')
            for p in policyList:
                promotion.append(p['content'])
            # bed []  bedType [] promotion[]
            result.append(room_entity(roomName, baseRoomId, roomId, roomSize, bed, bedType, roomFloor, hasDinning, hasWindows, payType, promotion))
    return result

if __name__ == '__main__':
    room('608516', '1', '2020-11-12', '2020-11-13', 1)
