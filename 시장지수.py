import time
import requests
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def 시장지수():
    now = time
    y = str(now.localtime().tm_year)
    m = int(now.localtime().tm_mon)
    d = int(now.localtime().tm_mday)
    d=d-1

    if d<10:
        d=str(d)
        d="0"+d
    if m<10:
        m=str(m)
        m="0"+m
    m=str(m)
    d=str(d)
    nowtime=y+m+d

    url1 = 'https://apis.data.go.kr/1160100/service/GetMarketIndexInfoService/getStockMarketIndex?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&resultType=json&numOfRows=2&idxNm=%EC%BD%94%EC%8A%A4%ED%94%BC'
    response = requests.get(url1).json()

    with open("시장지수\KOSPI.json", "w") as f:
        json.dump(response, f)
        

    with open("시장지수\KOSPI.json", "r") as f:
        data = json.load(f)
        
    #print(data)
    
    KOSPI고가 = data['response']['body']['items']['item'][0]['hipr']
    KOSPI저가 = data['response']['body']['items']['item'][0]['lopr']
    KOSPI시가 = data['response']['body']['items']['item'][0]['mkp']
    KOSPI종가 = data['response']['body']['items']['item'][0]['clpr']
    KOSPI거래량 = data['response']['body']['items']['item'][0]['trqu']
    
    KOSPI종가1 = data['response']['body']['items']['item'][1]['clpr']
    
    KOSPIm=float(KOSPI종가)-float(KOSPI종가1)
    if float(KOSPIm)<0:
        KOSPImt="▼"
    elif float(KOSPIm)>0:
        KOSPImt="▲"
    else:
        KOSPImt="="
    KOSPIm=str(KOSPIm)
    
    KOSPI지수mol="기준일:"+nowtime+"\n어제 KOSPI지수: "+KOSPI종가+"\n["+KOSPImt+KOSPIm+"]\n"+"  KOSPI시가: "+KOSPI시가+"\n"+"  KOSPI최고가: "+KOSPI고가+"\n"+"  KOSPI최저가: "+KOSPI저가+"\n"+"  KOSPI종가: "+KOSPI종가+"\n"+"  KOSPI거래량: "+KOSPI거래량+"\n\n\n"
    
    ##
    
    url2 = 'https://apis.data.go.kr/1160100/service/GetMarketIndexInfoService/getStockMarketIndex?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&resultType=json&numOfRows=2&idxNm=KRX%20300'
    response = requests.get(url2).json()

    with open("시장지수\KRX300.json", "w") as f:
        json.dump(response, f)
        

    with open("시장지수\KRX300.json", "r") as f:
        data = json.load(f)
        
    #print(data)
    
    KRX300고가 = data['response']['body']['items']['item'][0]['hipr']
    KRX300저가 = data['response']['body']['items']['item'][0]['lopr']
    KRX300시가 = data['response']['body']['items']['item'][0]['mkp']
    KRX300종가 = data['response']['body']['items']['item'][0]['clpr']
    KRX300거래량 = data['response']['body']['items']['item'][0]['trqu']
    
    KRX300종가1 = data['response']['body']['items']['item'][1]['clpr']
    
    KRX300m=float(KRX300종가)-float(KRX300종가1)
    if float(KRX300m)<0:
        KRX300mt="▼"
    elif float(KRX300m)>0:
        KRX300mt="▲"
    else:
        KRX300mt="="
    KRX300m=str(KRX300m)
    
    KRX300지수mol="기준일:"+nowtime+"\n어제 KRX300지수: "+KRX300종가+"\n["+KRX300mt+KRX300m+"]\n"+"  KRX300시가: "+KRX300시가+"\n"+"  KRX300최고가: "+KRX300고가+"\n"+"  KRX300최저가: "+KRX300저가+"\n"+"  KRX300종가: "+KRX300종가+"\n"+"  KRX300거래량: "+KRX300거래량+"\n\n\n"
        
    ##
    
    url3 = 'https://apis.data.go.kr/1160100/service/GetMarketIndexInfoService/getStockMarketIndex?serviceKey=kFg3740w8oA0URfa6U0acwTHl6OBznrukbTSF5qHxgELxjG2jtx2Z7ozqItFCHb%2FLTqdMYBKqbgoJyxHQSDatA%3D%3D&resultType=json&numOfRows=2&idxNm=%EC%BD%94%EC%8A%A4%EB%8B%A5'
    response = requests.get(url3).json()

    with open("시장지수\KOSDAQ.json", "w") as f:
        json.dump(response, f)
        

    with open("시장지수\KOSDAQ.json", "r") as f:
        data = json.load(f)
        
    #print(data)
    
    KOSDAQ고가 = data['response']['body']['items']['item'][0]['hipr']
    KOSDAQ저가 = data['response']['body']['items']['item'][0]['lopr']
    KOSDAQ시가 = data['response']['body']['items']['item'][0]['mkp']
    KOSDAQ종가 = data['response']['body']['items']['item'][0]['clpr']
    KOSDAQ거래량 = data['response']['body']['items']['item'][0]['trqu']
    
    KOSDAQ종가1 = data['response']['body']['items']['item'][1]['clpr']
    
    KOSDAQm=float(KOSDAQ종가)-float(KOSDAQ종가1)
    if float(KOSDAQm)<0:
        KOSDAQmt="▼"
    elif float(KOSDAQm)>0:
        KOSDAQmt="▲"
    else:
        KOSDAQmt="="
    KOSDAQm=str(KOSDAQm)
    
    KOSDAQ지수mol="기준일:"+nowtime+"\n어제 KOSDAQ지수: "+KOSDAQ종가+"\n["+KOSDAQmt+KOSDAQm+"]\n"+"  KOSDAQ시가: "+KOSDAQ시가+"\n"+"  KOSDAQ최고가: "+KOSDAQ고가+"\n"+"  KOSDAQ최저가: "+KOSDAQ저가+"\n"+"  KOSDAQ종가: "+KOSDAQ종가+"\n"+"  KOSDAQ거래량: "+KOSDAQ거래량+"\n\n\n"
    
    
    지수mol=KRX300지수mol+KOSPI지수mol+KOSDAQ지수mol
    
    print(지수mol)
    
    with open('mil_file\mol_G.txt', "w", encoding='utf-8') as f:
        data = 지수mol
        f.write(data)