import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def 환율():
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

    driver.get('https://www.kita.net/cmmrcInfo/ehgtGnrlzInfo/rltmEhgt.do')
    원달러 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[1]')
    원앤 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[1]')
    원유로 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[3]/td[1]')
    원위환 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[4]/td[1]')
    원홍콩 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[5]/td[1]')
    원영국 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[6]/td[1]')
    
    전일원달러 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[1]/td[2]')
    전일원앤 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[2]/td[2]')
    전일원유로 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[3]/td[2]')
    전일원위환 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[4]/td[2]')
    전일원홍콩 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[5]/td[2]')
    전일원영국 = driver.find_element("xpath",'/html/body/div[1]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[6]/td[2]')
    
    원달러=원달러.text
    원앤=원앤.text
    원유로=원유로.text
    원위환=원위환.text
    원홍콩=원홍콩.text
    원영국=원영국.text
    
    전일원달러=전일원달러.text
    전일원앤=전일원앤.text
    전일원유로=전일원유로.text
    전일원위환=전일원위환.text
    전일원홍콩=전일원홍콩.text
    전일원영국=전일원영국.text
    
    원달러="USD 1$ = "+원달러+"₩    (전일대비)"
    원앤="JPY 1￥ = "+원앤+"₩    (전일대비)"
    원유로="EUR 1€ = "+원유로+"₩    (전일대비)"
    원위환="CNY 1¥ = "+원위환+"₩    (전일대비)"
    원홍콩="HKD 1HK$ = "+원홍콩+"₩    (전일대비)"
    원영국="GBP 1£ = "+원영국+"₩    (전일대비)"

    mol_Y="\n-----------------\n\n"+nowtime+"\n\n"+원달러+전일원달러+"\n\n"+원앤+전일원앤+"\n\n"+원유로+전일원유로+"\n\n"+원위환+전일원위환+"\n\n"+원홍콩+전일원홍콩+"\n\n"+원영국+전일원영국
    with open('mil_file\mol_Y.txt', "w", encoding='utf-8') as f:
        data = mol_Y
        f.write(data)