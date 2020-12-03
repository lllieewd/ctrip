# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
import math
import csv
import time
from ctripV2 import Rateplan
import os
# 成都 28 绵阳 370  宜宾 514 凉山 7537 乐山 345 阿坝 1838 西安 10  咸阳  111 榆林 527 宝鸡 112 延安 110 汉中 129
cityMap = {'成都': 28, '绵阳': 370, '宜宾': 514, '凉山': 7537, '乐山': 345, '阿坝': 1838, '西安': 10, '咸阳': 111, '榆林': 527, '宝鸡': 112, '延安': 110, '汉中': 129}

if __name__ == '__main__':
    checkIn = '2020-11-12'
    checkOut = '2020-11-13'
    fileDir = '1112'
    pvid = 1
    folder = 'F:\\hotel\\ctripV2\\data\\1109'

    fileArr = []
    for root, dis, files in os.walk(folder):  # os.walk() 返回的是当前的路径，当前文件夹下的文件：
        for file in files:
            if '_hotel' in file:
                # print(file)
                fileArr.append(file)
    for file in fileArr:
        cityName = file.split("_")[0]
        cityId = cityMap[cityName]
        star = file.split("_")[2]
        print("开始取" + cityName + "_" + star + "的房间数据")
        with open(folder + '\\' + file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            lineNum = 0

            j = open('data\\'+fileDir+'\\' + cityName + '_' + checkIn + '_' + star + '_room.csv', 'w', encoding='utf-8', newline='')
            j_csv_writer = csv.writer(j)
            j_csv_writer.writerow(["酒店ID", "酒店名称", "房型ID", "房间ID", "日期", "客房房型", "客房面积", "床型分类", "床型规格",
                                   "楼层", "是否有窗户", "是否有早餐", "附加说明", "支付方式"])

            for row in reader:
                lineNum += 1
                if lineNum != 1:
                    hotelId = row[1]
                    hotelName = row[2]

                    # name, baseRoomId, roomId, area, bed, bedType, floor, hasDinning, hasWindows, payType, promotion
                    roomList = Rateplan.room(hotelId, cityId, checkIn, checkOut, pvid)
                    for room in roomList:
                        j_csv_writer.writerow(
                            [hotelId, hotelName, room.baseRoomId, room.roomId, checkIn, room.name, room.area, '、'.join(room.bedType), '、'.join(room.bed),
                             room.floor, room.hasWindows, room.hasDinning, '、'.join(room.promotion), room.payType])
                    pvid += 1
                    time.sleep(1)
        print("取完" + cityName + "_" + star + "的房间数据")
    print("完成")



