import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import requests
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def 금리():
    now = time
    y = str(now.localtime().tm_year)
    m = str(now.localtime().tm_mon)
    d = str(now.localtime().tm_mday)
    h = str(now.localtime().tm_hour)
    mi = str(now.localtime().tm_min)

    nowtime=y+"년"+m+"월"+d+"일"+h+"시"+mi+"분 기준"


    options = ChromeOptions()
    options.add_argument('headless')
    options.add_argument("disable-gpu")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("window-size=1920x1080")
    driver = webdriver.Chrome('chromedriver.exe', options=options)

    #

    driver.get('https://www.bok.or.kr/portal/main/main.do')
    기준금리dd1 = driver.find_element("xpath",'//*[@id="content"]/div/div/div[1]/div[2]/div[2]/dl/dd[1]')
    기준금리 = 기준금리dd1.text
    명목금리=기준금리.replace('%','')

    #

    driver.get('https://search.naver.com/search.naver?ie=UTF-8&sm=whl_sug&query=%EB%AC%BC%EA%B0%80%EC%83%81%EC%8A%B9%EB%A5%A0')
    물가상승률dd1 = driver.find_element("xpath",'/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[1]/div[1]/div[2]/div[2]/em')
    물가상승률 = 물가상승률dd1.text
    물가상승률퍼 = "+"+물가상승률
    물가상승률 = 물가상승률.replace('%','')

    #

    print('\033[37m'+"------------")
    print('\033[37m'+ "현재 시각:", '\033[93m'+nowtime)
    print('\033[37m'+"\n기준금리(현재): ", '\033[93m'+기준금리)
    print('\033[37m'+"\n물가상승률(전년동월대비): ", '\033[93m'+물가상승률퍼)
    print('\033[37m'+"------------")

    명목금리=float(명목금리)
    물가상승률=float(물가상승률)

    실질금리=명목금리-물가상승률
    print(실질금리)
    명목금리=str(명목금리)
    물가상승률=str(물가상승률)
    실질금리=str(실질금리)
    mol="\n-----------------\n\n"+nowtime+"\n\n"+"명목금리(기준금리): "+명목금리+"\n"+"PCI(물가상승률): "+물가상승률+"\n"+"실질금리: "+실질금리+"\n"

    with open('mil_file\mol.txt', "w", encoding='utf-8') as f:
        data = mol
        f.write(data)