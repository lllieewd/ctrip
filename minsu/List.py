# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import math
import csv
from minsu import Browser


def list_page(browser, cityUrl, checkIn, checkOut, page):
    url = "https://inn.ctrip.com/onlineinn/newlist/" + cityUrl + "/?d2=" + checkOut + "&d1=" + checkIn + "&p=" + str(
        page)
    browser.get(url)
    data = browser.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(data, features='html.parser')
    div = soup.find(name='div', attrs={"class": "innproducts-list-t2"})
    if div is None:
        return []
    a_list = div.find_all(name='a', attrs={"class": "tit"})
    hrefs = []
    for a in a_list:
        hrefs.append(a.get('href'))
    return hrefs


if __name__ == '__main__':
    # 成都 1000 绵阳	200 宜宾	150 凉山	400 乐山	400 阿坝	250 西安	800 咸阳	150 榆林	50 宝鸡	100 延安	100 汉中	100
    cityList = [['成都', 'chengdu10', 1000],
                ['绵阳', 'mianyang92', 200],
                ['宜宾', 'yibin95', 150],
                ['凉山', 'liangshan97', 400],
                ['乐山', 'leshan93', 400],
                ['阿坝', 'aba107', 250],
                ['西安', 'xian17', 800],
                ['咸阳', 'xianyang303', 150],
                ['榆林', 'yulinshi306', 50],
                ['宝鸡', 'baoji302', 100],li02
                ['延安', 'yanan25', 100],
                ['汉中', 'hanzhong305', 100]
                ]
    checkIn = '2020-11-10'
    checkOut = '2020-11-11'
    browser = Browser.get()
    for city in cityList:
        cityName = city[0]
        cityUrl = city[1]
        num = city[2]
        if num == 0:
            continue
        pageMax = math.ceil(num / 15)
        page = 1
        print(cityName + '开始收集' + str(pageMax) + '页')
        j = open('data\\1110\\' + cityName + '_' + checkIn + '_minsu.csv', 'w', encoding='utf-8', newline='')
        j_csv_writer = csv.writer(j)
        result = []
        while page <= pageMax:
            hrefs = list_page(browser, cityUrl, checkIn, checkOut, page)
            if hrefs.__len__() == 0:
                print(cityName + "取第" + str(page) + "获取为空")
                break
            for href in hrefs:
                result.append(href)
            page += 1
        result = list(set(result))
        for href in result:
            j_csv_writer.writerow([href])
        print(cityName + '收集完成')
    print('任务结束')
    browser.quit()
