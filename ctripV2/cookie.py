# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
def getCookie():
    # return '_abtest_userid=4ccac489-1aa8-471a-bb53-3a138df46c35; intl_ht1=h4=112_8056970; _bfa=1.1604387080417.g1lpx.1.1604387080417.1604387080417.1.1; _bfs=1.1'
    return '_abtest_userid=997c988c-7e80-4cb4-b840-d08bdc8709b6; _ga=GA1.2.1973624881.1573724682; _RGUID=5f8141a5-c0e6-4393-b957-21d437f05d0f; _RDG=2830c1f470342329b6292bc1632e179328; _RSG=JEav0NQG1.5Fq5ytGT8NbB; MKT_CKID=1579673323829.cwan2.87f3; ibulanguage=CN; ibulocale=zh_cn; cookiePricesDisplayed=CNY; MKT_Pagesource=PC; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; login_uid=3339EA84EF40BB005928991942C98374; login_type=0; IsPersonalizedLogin=F; UUID=7F3C1371649143E3B88DD942930DF66F; nfes_isSupportWebP=1; nfes_isSupportWebP=1; MKT_OrderClick=ASID=4897155952&AID=4897&CSID=155952&OUID=index&CT=1604652199444&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155952%26allianceid%3D4897%26ouid%3Dindex&VAL={"pc_vid":"1573724678415.2ku552"}; Union=SID=155952&AllianceID=4897&OUID=index; _gid=GA1.2.1114939717.1604889221; MKT_CKID_LMT=1604889221340; _RF1=119.130.104.121; HotelCityID=112split%E5%AE%9D%E9%B8%A1splitBaojisplit2020-11-9split2020-11-10split0; intl_ht1=h4=111_632075,28_25680819,110_66848974,129_12090704,28_472757,28_470094; _bfi=p1%3D102003%26p2%3D102003%26v1%3D406%26v2%3D405; _jzqco=%7C%7C%7C%7C1604889221532%7C1.1752613493.1573724681772.1604913888671.1604918411107.1604913888671.1604918411107.undefined.0.0.228.228; appFloatCnt=209; __zpspc=9.29.1604918411.1604918411.1%232%7Cwww.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%7C%23; _bfa=1.1573724678415.2ku552.1.1604910462269.1604918402547.26.407.212094; _bfs=1.2; _uetsid=77e786f0223711ebbba3f99ec98ec43e; _uetvid=1c73e2f01cd611eb8a99af0b95a5e265'


def getClientId():
    return "1573724678415.2ku552"


def getUserIp():
    return "119.130.104.121"


def getCookieDict():
    cookie = getCookie()
    arr = []

    for i in cookie.split('; '):
        cookie_dic = dict(name=i.split('=')[0], value=i.split('=')[1], domain='.ctrip.com')
        arr.append(cookie_dic)
    return arr

