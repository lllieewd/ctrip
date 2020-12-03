# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import math
import csv
from minsu import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from minsu.items import minsu_details
from selenium.common.exceptions import TimeoutException
import time
import MySQLdb


def get_details(browser, hotelId, checkIn, checkOut):
    url = "https://inn.ctrip.com/onlineinn/newdetail/"+hotelId+"?d1="+checkIn+"&d2="+checkOut
    browser.get(url)
    element = WebDriverWait(browser, 4).until(
        EC.presence_of_element_located((By.CLASS_NAME, "txt-price"))
    )
    # data = element.get_attribute('innerHTML')
    data = browser.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(data, features='html.parser')
    # hotelId, cityName, hotelName, price, realPrice, discounts, landlord, landlordType, rentType, rentDescription, houseType,
    # houseDescription, personNum, bedInfo, hasWifi, hasParty, hasBusiness, location, viewInfo, trainInfo, trainDistance, planeInfo,
    # planeDistance, hotelDescription, score, commentNum, cashPledge, cleanFee, rule, tag

    titleInfo = soup.find(name='div', attrs={"class": "innproduct-breadcrumbs"})
    cityName = titleInfo.find(name='h4', attrs={"class": "txt"}).text

    nameInfo = soup.find(name='div', attrs={"class": "con-0"})
    hotelName = nameInfo.find(name='div', attrs={"class": "tit"}).text
    tag = []
    tagsDiv = nameInfo.find(name='div', attrs={"class": "tags"})
    tagList = tagsDiv.find_all(name='div', attrs={"class": "item item-type-0"})
    for tagItem in tagList:
        tag.append(tagItem.text)
    priceInfo = soup.find(name="div", attrs={"class": "con-price"})
    realPrice = priceInfo.find(name="div", attrs={"class": "txt-price"}).text
    priceItem = priceInfo.find(name="span", attrs={"class": "txt-price-origin"})
    price = ''
    if priceItem is not None:
        price = priceItem.text
    activityInfo = soup.find(name="div", attrs={"class": "innproduct-activity-s2"})
    discounts = ''
    if activityInfo is not None:
        activityItem = activityInfo.find_all(name='div', attrs={"class": "item"})
        for activity in activityItem:
            tagSpan = activity.find(name='span', attrs={"class": "tag"})
            if tagSpan.text == '连住优惠':
                txtSpan = activity.find(name='span', attrs={"class": "txt"})
                discounts = txtSpan.text
    landlordInfo = soup.find(name='div', attrs={"class": "innproduct-landlord"})
    landlord = landlordInfo.find(name='div', attrs={"class": "tit"}).text
    landlordType = []
    conTag = landlordInfo.find(name='div', attrs={"class": "con-tag"})
    landloadList = conTag.find_all(name='span', attrs={"class": "item"})
    for item in landloadList:
        landlordType.append(item.text)
    baseInfo = soup.find(name='div', attrs={"class": "innproduct-base"})
    baseList = baseInfo.find_all(name='div', attrs={"class": "item"})
    rentType = baseList[0].find(name='span', attrs={"class": "tit"}).text
    rentDescription = baseList[0].find(name='span', attrs={"class": "txt"}).text
    houseType = baseList[1].find(name='span', attrs={"class": "tit"}).text
    houseDescription = baseList[1].find(name='span', attrs={"class": "txt"}).text
    personNum = baseList[2].find(name='span', attrs={"class": "tit"}).text
    bedList = baseList[2].find_all(name='span', attrs={"class": "txt"})
    bedInfo = []
    for bedItem in bedList:
        bedInfo.append(bedItem.text)
    # hasWifi, hasParty, hasBusiness, location, viewInfo, trainInfo, trainDistance, planeInfo,
    # planeDistance, hotelDescription, score, commentNum, cashPledge, cleanFee, rule, tag
    wifiDevice = soup.find(name='div', attrs={"class": "item item-device-e062"})
    hasWifi = '否'
    if wifiDevice is not None:
        hasWifi = '是'
    ruleInfo = soup.find(name='div', attrs={"class": "innproduct-rule"})
    ruleList = ruleInfo.find_all(name='div', attrs={"class": "item"})
    hasParty = '否'
    hasBusiness = '否'
    cashPledge = ''
    for ruleItem in ruleList:
        ruleTxt = ruleItem.find(name='div', attrs={"class": "txt-lbl"}).text
        if ruleTxt == '押金':
            cashPledge = ruleItem.find(name='div', attrs={"class": "txt-val"}).text
        if ruleTxt == '房屋守则':
            valList = ruleItem.find_all(name='span', attrs={"class": "item"})
            for valItem in valList:
                valTxt = valItem.text
                classTxt = valItem.get('class')
                if valTxt == '可以聚会' and 'disabled' not in classTxt:
                    hasParty = '是'
                if valTxt == '允许商业拍摄' and 'disabled' not in classTxt:
                    hasBusiness = '是'
    mapInfo = soup.find(name='div', attrs={"class": "innproduct-map"})
    viewInfo = ''
    trainInfo = ''
    trainDistance = ''
    planeInfo = ''
    planeDistance = ''
    if mapInfo is not None:
        location = mapInfo.find(name='div', attrs={"class": "txt-address"}).text
        viewDiv = mapInfo.find(name='div', attrs={"class": "item item-map-1"})
        if viewDiv is not None:
            viewInfo = viewDiv.text
        trainDiv = mapInfo.find(name='div', attrs={"class": "item item-map-3"})
        if trainDiv is not None:
            trainInfo = trainDiv.find(name='div', attrs={"class": "tit"}).text
            trainDistance = trainDiv.find(name='div', attrs={"class": "txt"}).text
        planeDiv = mapInfo.find(name='div', attrs={"class": "item item-map-4"})
        if planeDiv is not None:
            planeInfo = planeDiv.find(name='div', attrs={"class": "tit"}).text
            planeDistance = planeDiv.find(name='div', attrs={"class": "txt"}).text
    else:
        locationDiv = soup.find(name='div', attrs={"class": "con-location"})
        location = locationDiv.find(name='span', attrs={"class": "item"})
    hotelInfo = soup.find(name='div', attrs={"class": "innproduct-description"})
    hotelList = hotelInfo.find_all(name='div', attrs={"class": ""})
    hotelDescription = []
    for hotelItem in hotelList:
        if hotelItem is not None and hotelItem.text != '':
            hotelDescription.append(hotelItem.text)
    commentInfo = soup.find(name='div', attrs={"class": "innproduct-comment"})
    score = ''
    commentNum = ''
    if commentInfo is not None:
        commentDetails = commentInfo.find(name='div', attrs={"class": "con-info"})
        score = commentDetails.find(name='span', attrs={"class": "val"}).text
        commentNum = commentDetails.find(name='span', attrs={"class": "txt-num"}).text
    feeInfo = soup.find(name='div', attrs={"class": "innproduct-fee"})
    feeList = feeInfo.find_all(name='div', attrs={"class": "item item-type-0"})
    cleanFee = ''
    rule = ''
    for feeItem in feeList:
        feeTxt = feeItem.find(name='div', attrs={"class": "txt-lbl"}).text
        if feeTxt == '清洁费':
            cleanFee = feeItem.find(name='div', attrs={"class": "txt-val"}).text
        if feeTxt == '加人':
            rule = feeItem.find(name='div', attrs={"class": "txt-val"}).text
    return minsu_details(hotelId, cityName, hotelName, price, realPrice, discounts, landlord, landlordType, rentType, rentDescription, houseType,
                         houseDescription, personNum, bedInfo, hasWifi, hasParty, hasBusiness, location, viewInfo, trainInfo, trainDistance, planeInfo,
                         planeDistance, hotelDescription, score, commentNum, cashPledge, cleanFee, rule, tag)


if __name__ == '__main__':
    checkIn = '2020-11-27'
    checkOut = '2020-11-28'
    browser = Browser.get()
    filePath = 'F:\\hotel\\minsu\\data\\1110\\minsuid.csv'
    db = MySQLdb.connect("47.99.91.152", "root", "123456", "hotel", charset='utf8')
    db.autocommit(on=True)
    cursor = db.cursor()
    r = cursor.execute("SELECT * FROM minsu_info")
    result = cursor.fetchall()

    j = open('data\\' + checkIn + '_minsu.csv', 'a+', encoding='gbk', newline='', errors='ignore')
    j_csv_writer = csv.writer(j)
    # j_csv_writer.writerow(["民宿ID", "城市", "房间名称", "实际价格", "价格", "连住优惠", "房东名称", "房东类型", "出租类型",
    #                        "出租类型描述", "户型", "户型描述", "宜住人数", "床型及数量", "是否提供WIFI",
    #                        "是否可聚会", "是否可商业拍摄", "地理位置", "附近景点数量及距离描述", "附近火车站", "直线车站距离*km", "附近机场",
    #                        "直线机场距离*km", "房屋描述", "评分", "评价数", "押金", "清洁费", "加人规则", "标签"])
    num = 0
    for x in result:
        x_id = x[0]
        su_id = x[1]
        su_date = x[2]
        if su_date == checkIn:
            continue

        try:
            details = get_details(browser, su_id, checkIn, checkOut)
        except TimeoutException:
            print('查找超时:' + su_id)
            continue
        j_csv_writer.writerow([details.hotelId, details.cityName, details.hotelName, details.realPrice, details.price,
                               details.discounts, details.landlord, ' '.join(details.landlordType), details.rentType,
                               details.rentDescription, details.houseType, details.houseDescription, details.personNum, ' '.join(details.bedInfo),
                               details.hasWifi, details.hasParty, details.hasBusiness, details.location,
                               details.viewInfo, details.trainInfo, details.trainDistance, details.planeInfo, details.planeDistance,
                               '\n'.join(details.hotelDescription), details.score, details.commentNum, details.cashPledge,
                               details.cleanFee, details.rule, ' '.join(details.tag)])
        cursor.execute("UPDATE minsu_info SET check_in='"+checkIn+"' WHERE id="+str(x_id))
        num += 1
        if num % 300 == 0:
            print('已取' + str(num))
            time.sleep(40)
        elif num % 100 == 0:
            print('已取' + str(num))
            time.sleep(10)
        else:
            time.sleep(1.5)
    print('任务结束')
    db.close()
    browser.quit()
