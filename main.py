#-*- coding: utf-8 -*-
import inspect, os, platform, time
from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from 금리 import *
from 시장지수 import *
from 환율 import *
from 대형지분공시 import *
import urllib.request
import json,csv

tk = Tk()
tk.title("통합 투자 정보 지원 프로그램")
tk.resizable(False, False)
widget = Label(tk, text="통합 투자 정보 지원 프로그램",font=('BRLNSB', 20),padx=1050,highlightthickness=4,highlightbackground='gray',background='gray',foreground='#ffffff')
widget.pack()
widget = Label(tk, text="",font=('BRLNSB', 20),pady=450,padx=1230,highlightthickness=4,highlightbackground='gray',background='gray',foreground='#ffffff')
widget.pack()
#
widgetl1 = Label(tk, text="금리조회",font=('BRLNSB', 10),padx=145,highlightthickness=4,highlightbackground='gray',background='gray',foreground='#ffffff')
widgetl2 = Label(tk, text="시장지수",font=('BRLNSB', 10),padx=150,highlightthickness=4,highlightbackground='gray',background='gray',foreground='#ffffff')
widgetl3 = Label(tk, text=" 환율 ",font=('BRLNSB', 10),padx=116,highlightthickness=4,highlightbackground='gray',background='gray',foreground='#ffffff')
widgetl4 = Label(tk, text="기업실적 & 대형 지분공시",font=('BRLNSB', 10),padx=166,highlightthickness=4,highlightbackground='gray',background='gray',foreground='#ffffff')
widgetl1.place(x=10,y=45)
widgetl2.place(x=385,y=45)
widgetl3.place(x=780,y=45)
widgetl4.place(x=1085,y=45)
#
widget1 = Text(tk, width=50, height=50)
widget2 = Text(tk, width=50, height=50)
widget3 = Text(tk, width=45, height=50)
widget4 = Text(tk, width=200, height=50)
widget1.pack(side="left",padx=10, pady=20)
widget2.pack(side="left",padx=10, pady=30)
widget3.pack(side="left",padx=10, pady=30)
widget4.pack(side="left",padx=10, pady=30)
widget1.place(x=10,y=75)
widget2.place(x=385,y=75)
widget3.place(x=758,y=75)
widget4.place(x=1100,y=75)
#
ent1=Entry(tk)
ent1.place(x=1305,y=70)
ent1.pack(padx=50, pady=50)

def time_event():
    button1['text'] = ('계산중..')
    now = time
    y = str(now.localtime().tm_year)
    m = str(now.localtime().tm_mon)
    d = str(now.localtime().tm_mday)
    h = str(now.localtime().tm_hour)
    mi = str(now.localtime().tm_min)
    se= str(now.localtime().tm_sec)

    nowtime=y+"년"+m+"월"+d+"일"+h+"시"+mi+"분"+se+"초 기준"
    print("현재시간: ",nowtime)
    button1['text'] = ('서버시간:',nowtime)
    
        
def event():
    금리()
    with open('mil_file\mol.txt', "r", encoding='utf-8') as f: #txt읽기
        mol = f.read()
        f.close()
    widget1.insert(1.0, mol)
    widget1.pack(side="left",padx=10, pady=20)
    widget1.place(x=10,y=75)

def a_event(): #시장지수
    시장지수()
    with open('mil_file\mol_G.txt', "r", encoding='utf-8') as f: #txt읽기
        mol_g = f.read()
        f.close()
    widget2.insert(1.0, mol_g)
    widget2.pack(side="left",padx=10, pady=30)
    widget2.place(x=385,y=75)

    
def b_event():  #환율
    환율()
    with open('mil_file\mol_Y.txt', "r", encoding='utf-8') as f: #txt읽기
        mol_y = f.read()
        f.close()
    widget3.insert(1.0, mol_y)
    widget3.pack(side="left",padx=10, pady=30)
    widget3.place(x=758,y=75)
    button4['text'] = ('계산완료')
    time.sleep(2)
    button4['text'] = ('환율 조회')
    
def c_event():   #지분공시
    coper=ent1.get()
    
    with open('지분공시\coper.txt', "w", encoding='utf-8') as f:
        data = coper
        f.write(data)
        
    now = time
    d = str(now.localtime().tm_mday)
    h = str(now.localtime().tm_hour)
    mi = str(now.localtime().tm_min)

    지분공시()
    
    xf=d+h+mi+'mol_P.xlsx'
    df = pd.read_excel(xf,usecols=[2,4,5,6,7,8,9,10,11,12])
        
    widget4.insert(0.5, df)
    widget4.pack(side="left",padx=10, pady=50)
    widget4.place(x=1100,y=75)
    
    
    
button1 = Button(tk, text='시간조회', command=time_event)
button2 = Button(tk, text='금리 조회', command=event, state="normal")
button3 = Button(tk, text='시장지수 조회', command=a_event)
button4 = Button(tk, text='환율 조회', command=b_event, state="normal")
button5 = Button(tk, text='지분공시 조회', command=c_event, state="normal")


button1.pack(side="bottom",padx=60, pady=30)

button2.pack(side="bottom", padx=30, pady=30)
button3.pack(side="bottom",padx=30, pady=30)
button4.pack(side="bottom", padx=30, pady=30)
button5.pack(side="bottom", padx=30, pady=30)
button1.place(x=1700,y=10)

button2.place(x=160,y=750)
button3.place(x=515,y=750)
button4.place(x=875,y=750)
button5.place(x=1195,y=750)

tk.mainloop()