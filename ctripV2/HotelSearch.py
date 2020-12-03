# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import json
import uuid
from ctripV2.items import list_entity

import requests

from ctripV2 import cookie

uid = str(uuid.uuid4())
suid = ''.join(uid.split('-'))


def hotel_search(start_date, end_date, city_name, city_id, pvid, star, page_no):
    url = "https://m.ctrip.com/restapi/soa2/16709/json/HotelSearch?testab=" + suid
    headers = {
        'authority': 'm.ctrip.com',
        'method': 'POST',
        'path': '/restapi/soa2/16709/json/hote1search?testab=' + suid,
        'scheme': 'https',
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
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

    payload = {
        "meta": {
            "fgt": "",
            "hotelId": "",
            "priceToleranceData": "",
            "priceToleranceDataValidationCode": "",
            "mpRoom": [],
            "hotelUniqueKey": "",
            "shoppingid": "",
            "minPrice": "",
            "minCurr": ""
        },
        "seqid": "",
        "deduplication": [],
        "filterCondition": {
            "star": [star],
            "rate": "",
            "rateCount": [],
            "priceRange": {
                "lowPrice": 0,
                "highPrice": -1
            },
            "priceType": "",
            "breakfast": [],
            "payType": [],
            "bedType": [],
            "bookPolicy": [],
            "bookable": [],
            "discount": [],
            "zone": [],
            "landmark": [],
            "metro": [], "airportTrainstation": [], "location": [], "cityId": [], "amenty": [], "promotion": [],
            "category": [], "feature": [], "brand": [], "popularFilters": [], "hotArea": [], "ctripService": []},
        "searchCondition": {"sortType": "1", "adult": 1, "child": 0, "age": "", "pageNo": page_no, "optionType": "City",
                            "optionId": city_id,
                            "lat": 0, "destination": "", "keyword": "", "cityName": city_name, "lng": 0,
                            "cityId": city_id, "checkIn": start_date, "checkOut": end_date, "roomNum": 1,
                            "mapType": "gd", "travelPurpose": 0, "countryId": 1,
                            "url": "",
                            # https://hotels.ctrip.com/hotels/list?city=1&checkin=2020/11/02&checkout=2020/11/03&optionId=1&optionType=City&directSearch=0&display=%E5%8C%97%E4%BA%AC&crn=1&adult=1&children=0&searchBoxArg=t&travelPurpose=0&ctm_ref=ix_sb_dl&domestic=1&&starlist=5,4,3,2&highPrice=-1&barCurr=CNY&sort=1
                            "pageSize": 10, "timeOffset": 28800, "radius": 0, "directSearch": 0, "signInHotelId": 0,
                            "signInType": 0}, "queryTag": "NORMAL", "genk": True,
        "genKeyParam": {"a": 0, "b": start_date, "c": end_date, "d": "zh-cn", "e": 2}, "webpSupport": True,
        "platform": "online", "pageID": "102002",
        "head": {"Version": "", "userRegion": "CN", "Locale": "zh-CN", "LocaleController": "zh-CN", "TimeZone": "8",
                 "Currency": "CNY", "PageId": "102002", "webpSupport": True, "userIP": cookie.getUserIp(),
                 "P": "61884674695",
                 "ticket": "", "clientID": cookie.getClientId(), "group": "ctrip",
                 "Frontend": {"vid": cookie.getClientId(), "sessionID": 5, "pvid": pvid},
                 "Union": {"AllianceID": "", "SID": "", "Ouid": ""},
                 "HotelExtension": {"group": "CTRIP", "hasAidInUrl": False, "Qid": "463646314245", "WebpSupport": True,
                                    "hotelUuidKey": "FD4wp7KoLedTESqWcY8zYobE7Y3Me1nEUmjHnWFYbhRNSiMBwt1jSYtDjA1KhcvHGEaYkDjF3RMFKmljoY61RNHrD0IA3R79KBoYmDYqNjoLyHY0Xe5bwPlYlXw7lWXPenGitGY4YcYBFvX3ephYnOic8YDYHYkNIc5WdYDAY3GePOi0fInOj7YNcE7tvo6YOZwcnYpfJA9Y84wLYgMRFfwHOWfsE8HilQWhHvq9Y7bR10Jp6vzFvX9WUYPZEfox4QR3URa1v8GY3Nj5Myaqi0Pvh7Y3PjXgj5PiQgykNinY9DRDBJFGyMli5Gy6zYO6E3nw1GydhjA3EHzRbgJhYM7j1fwM0v74j6YlcYzPJXgwtXWZHe6AR0tW61jzHWLYSTYbcJ3SwX7W8Mep8R5ZWk5EhcWAYqHR3GwonWmDEQ6ikAWpFvnzR5QYU9iBcYz5Rmb"
                                    }
                 }
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)  # formData,
    r.raise_for_status()
    r.encoding = r.apparent_encoding

    json_data = json.loads(r.text)
    # print(json_data)
    result = []
    respone = json_data['Response']
    if dict(respone).get('hotelList') is None:
        return result
    hotel_list = respone['hotelList']['list']
    for hotel in hotel_list:
        hotel_id = hotel['base']['hotelId']
        hotel_name = hotel['base']['hotelName']
        star = hotel['base']['star']
        city_name = hotel['position']['cityName']
        position_area = dict(hotel['position']).get('area')
        result.append(list_entity(hotel_name, hotel_id, star, city_name, position_area))
    return result


if __name__ == '__main__':
    hotel_search('2020-11-05', '2020-11-06', '成都', '28', 1, 5, 15)
