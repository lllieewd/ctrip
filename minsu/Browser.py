# -*- coding: <encoding name> -*- : # -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains


accountName = '18777197236'
accountPass = 'xiecheng@1110'

def get():
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    browser = webdriver.Chrome(executable_path='D:\\chromedriver.exe', chrome_options=chrome_options)
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                    Object.defineProperty(navigator, 'webdriver', {
                      get: () => undefined
                    })
                  """
    })
    browser.implicitly_wait(30)
    browser.get('https://passport.ctrip.com/user/login')

    browser.find_element_by_id('nloginname').send_keys(accountName)
    browser.find_element_by_id('npwd').send_keys(accountPass)
    time.sleep(1.5)

    if browser.find_element_by_xpath("//span[@class='cpt-info-board']").text == "请按住滑块，拖动到最右":
        print("需要滑动验证码")
        time.sleep(2)
        button = browser.find_element_by_class_name("cpt-drop-btn")

        length = browser.find_element_by_xpath("//dd[@id='sliderddnormal']").size["width"]
        button_length = browser.find_element_by_class_name("cpt-drop-btn").size["width"]
        sliding_length = int(length) - int(button_length)

        action = ActionChains(browser)
        action.click_and_hold(button).perform()
        action.move_by_offset(sliding_length, 0).perform()
        time.sleep(1.5)
        if browser.find_element_by_class_name("cpt-choose-msg"):
            print("需要点击验证码验证")
            pass
    else:
        time.sleep(2)
        browser.find_element_by_id("nsubmit").click()
    print('等待 输入或跳转20s')

    time.sleep(20)
    return browser

