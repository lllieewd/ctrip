# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
from ctripV2 import GetReviewList
from ctripV2 import HotelPlaceInfo
from ctripV2 import HotelSearch
from ctripV2 import HotelStaticInfo
from ctripV2 import info
from ctripV2 import brand
from ctripV2 import Rateplan
import math
import csv
import time

if __name__ == '__main__':
    startDate = '2020-11-10'
    endDate = '2020-11-11'
    # 成都 28 绵阳 370  宜宾 514 凉山 7537 乐山 345 阿坝 1838 西安 10  咸阳  111 榆林 527 宝鸡 112 延安 110 汉中 129
    cityList = [
        # ['成都', 28,  124, 400, 500, 600],
        # ['绵阳', 370, 6, 59, 97, 200],
        # ['宜宾', 514, 5, 23, 61, 150],
        ['凉山', 7537, 6, 46, 120, 200],
        ['乐山', 345, 13, 99, 113, 300],
        ['阿坝', 1838, 16, 69, 161, 300],
        ['西安', 10, 71, 200, 300, 500],
        ['咸阳', 111, 1, 21, 82, 150],
        ['榆林', 527, 4, 30, 66, 150],
        ['宝鸡', 112, 6, 27, 63, 150],
        ['延安', 110, 6, 62, 92, 150],
        ['汉中', 129, 1, 39, 84, 150]
    ]
    pvid = 1

    for l in cityList:
        cityname = l[0]
        cityid = l[1]

        for star in [5, 4, 3, 2]:
            num = l[5 - star + 2]
            if num == 0:
                continue

            j = open('data\\1109\\' + cityname + '_' + startDate + '_' + str(star) + '_hotel.csv', 'w', encoding='utf-8', newline='')
            j_csv_writer = csv.writer(j)
            f = open('data\\1109\\' + cityname + '_' + startDate + '_' + str(star) + '_brand.csv', 'w', encoding='utf-8', newline='')
            f_csv_writer = csv.writer(f)
            j_csv_writer.writerow(["城市", "酒店ID", "酒店名称", "星级", "酒店类型", "开业时间", "装修时间", "房间数", "是否提供WIFI",
                                   "是否停车场", "是否提供接机服务", "商圈数据", "距离机场距离", "附近火车站距离", "距离地铁距离",
                                   "区域位置描述", "酒店简介", "评分", "评价数", "评价关键词", "所属集团", "特色"])
            f_csv_writer.writerow(["城市", "酒店名称", "所属集团", "品牌"])

            pageMax = math.ceil(num / 10)
            pageno = 1
            print(cityname + '：开始统计 星级' + str(star) + '，共' + str(pageMax) + '页')
            while pageno <= pageMax:
                # start_date, end_date, city_name, city_id, pvid, star, page_no
                cityList = HotelSearch.hotel_search(startDate, endDate, cityname, cityid, pvid, star, pageno)
                if cityList.__len__() == 0:
                    pageno += 1
                    continue

                for list_entity in cityList:
                    pvid += 1
                    static_entity = HotelStaticInfo.static(list_entity.hotelId, cityid, pvid)
                    place_entity = HotelPlaceInfo.place(list_entity.hotelId, cityid, pvid)
                    review_entity = GetReviewList.hotel_review(list_entity.hotelId, pvid)
                    info_entity = info.info(list_entity.hotelId, startDate, endDate, cityid)
                    brand_entity = brand.brand(list_entity.hotelId)
                    # 写基本信息
                    j_csv_writer.writerow(
                        [list_entity.cityName, list_entity.hotelId, list_entity.hotelName, list_entity.star,
                         brand_entity.hotel_title, static_entity.openDate, static_entity.renovationDate,
                         static_entity.roomNum, static_entity.hasWifi, static_entity.hasParking, static_entity.hasPlane,
                         list_entity.positionArea, info_entity.flight_distance, info_entity.train_distance,
                         info_entity.subway_distance, info_entity.place_info, static_entity.description,
                         review_entity.score, review_entity.totalReviews, '、'.join(review_entity.keywords),
                         brand_entity.group_name, '、'.join(brand_entity.brand)])

                    # 品牌信息
                    f_csv_writer.writerow(
                        [list_entity.cityName, list_entity.hotelName, brand_entity.group_name, '、'.join(brand_entity.brand)])
                print(cityname + "：第" + str(pageno) + "页数据取完")
                pageno += 1
                time.sleep(2)
            j.close()
            f.close()
    print('完成')
