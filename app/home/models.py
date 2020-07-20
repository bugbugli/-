import xml.etree.ElementTree as ET
import requests
import datetime
import pandas as pd
import pandas_datareader.data as web
import json
import numpy as np
import math


GMRIDStr = "BDWI"
GMRID = "1111775049"
TokenString = "143986D99078C7FAA845A8F36213E20CFD01C6469E8C2B1E077174064F5F1F659B94A985EAF4C1FA5834730E893878F94E17371C1A577F86361C18C8CF6BC5A14355A03D667408028B4CF3F9856307EB6C1C51A36CA0A8CA10F78851799113D9C1C5C3122F803EFC6FA6CDBDDBB70310C9A590981DD51D3A57E0B0FED68356899DB75FF992C8BA7FB12CC62405150265"


def goods():#資產
    goods_url = "http://61.220.30.176/weborder/autotrade.asmx/QueryTodayPositionGve3XML_NS?TokenString="+TokenString+"&Language=TC&SubTotalItem=&SortItem=AssetCode%20Asc"
    goods_response = requests.get(goods_url)

    root1=ET.fromstring(goods_response.text)

    lista = root1.text.replace('"','').split('/>')  #頭尾不要

    count = 0
    listb = []

    for i in range(len(lista)-1):
        listb.append([])
    i = 0
    for x in lista:
    	if i!=(len(lista)-1):
    		listb[count].append(x[x.find("I AssetID")+10:x.find(" Hold")])#商品代碼
    		listb[count].append(x[x.find("CompName")+9:x.find(" comptype=")])#商品名稱
    		listb[count].append(x[x.find("Hold")+5:x.find(" Available")][:-5])#持有數量
    		listb[count].append(x[x.find("Cost")+5:x.find("SettleCost")])#持有成本
    		listb[count].append(x[x.find("QuotePrice")+11:x.find(" PL")][:-2])#現價
    		listb[count].append(x[x.find("UpDown=")+7:x.find(" UnRealizedPL")][:-2])
    		listb[count].append(x[x.find("PL")+3:x.find(" UpDown")])
    		listb[count].append(x[x.find("UnRealizedPL")+13:x.find(" MarketValue")][:-7])
    		listb[count].append(x[x.find("MarketValue")+12:x.find(" CompName")][:-7])
    		listb[count].append(int(x[x.find("HoldPercent")+14:x.find("HoldPercent")+18])/100)
    		#print(listb[count],end='\n\n')
    		count+=1;
    	i+=1
    return listb

def CommissionReturn():#委託回報
    commision_url = "http://61.220.30.176/weborder/autotrade.asmx/QueryWaitingOrderListGVE3XML_NS?TokenString="+TokenString+"&Language=TC"

    commision_response = requests.get(commision_url)
    root1=ET.fromstring(commision_response.text)
    lista = root1.text.replace('"','').split('/>')  #頭尾不要

    count = 0
    listb = []
    #print(len(lista))
    if len(lista)<=2 and lista[0].find("OrderStatus")==-1:#若沒有資料直接回傳空list
        return listb
    else:
        for i in range(len(lista)-1):
        	listb.append([])
        i = 0
        for x in lista:
            if i!=(len(lista)-1) and x[x.find("OrderStatus")+12:x.find(" AllowUserCancel")]!='1':#不做最後一個且委託狀態為待處理單
                listb[count].append(x[x.find("AssetID")+8:x.find(" Price")])#公司代碼
                listb[count].append(x[x.find("CompName")+9:x.find(" CompType")])#公司名稱

                orderType=x[x.find("OrderType")+10:x.find(" OrderTime")]#掛單類型
                if orderType == "LMTU":
                    listb[count].append("漲停價")
                elif orderType == "LMTD":
                    listb[count].append("跌停價")
                elif orderType == "LMT":
                    listb[count].append("限價單")
                elif orderType == "MKT":
                    listb[count].append("期權市價單")

                BSAction=x[x.find("BSAction")+9:x.find(" OrderType")]#買/賣
                if BSAction  == "B ":
                    listb[count].append("普通買進")
                elif BSAction  == "S ":
                    listb[count].append("普通賣出")
                elif BSAction  == "MB":
                    listb[count].append("融資買入")
                elif BSAction  == "RB":
                    listb[count].append("融資賣出")
                elif BSAction  == "RS":
                    listb[count].append("融券買入")
                elif BSAction  == "MS":
                    listb[count].append("融券賣出")

                listb[count].append(float(x[x.find("Price")+6:x.find(" Volume")]))#委託價
                listb[count].append(x[x.find("Volume")+7:x.find(" BSAction")][:-5])#量/股
                #print(listb[count],end='\n\n')
                count+=1;
            i+=1
        return listb

def DealReturn():#成交回報
    today = str(datetime.date.today())
    today = today.replace('-','/')

    deal_url = "http://61.220.30.176/weborder/autotrade.asmx/QueryDealLogGVE3ByGMRDayRangeLiteXML_NS?GMRID="+GMRID+"&StartDate="+today+"&EndDate="+today+"&Language=TC"

    deal_response = requests.get(deal_url)
    root1=ET.fromstring(deal_response.text)
    lista = root1.text.replace('"','').split('/>')  #頭尾不要

    count = 0
    listb = []
    if len(lista)<=2 and lista[0].find("AssetCode")==-1:
        return listb
    else:
        for i in range(len(lista)-1):
        	listb.append([])


        i = 0
        for x in lista:
            if i!=(len(lista)-1):#不做最後一個
                listb[count].append(x[x.find("AssetCode")+10:x.find(" Price")])#公司代碼
                listb[count].append(x[x.find("CompName")+9:x.find(" logdesc")])#公司名稱

                orderType=x[x.find("OrderType")+10:x.find(" PFLAssetID")]#掛單類型
                if orderType == "LMTU":
                    listb[count].append("漲停價")
                elif orderType == "LMTD":
                    listb[count].append("跌停價")
                elif orderType == "LMT":
                    listb[count].append("限價單")
                elif orderType == "MKT":
                    listb[count].append("期權市價單")

                BSAction=x[x.find("BSAction")+9:x.find(" OrderType")]#買/賣
                if BSAction  == "B ":
                    listb[count].append("普通買進")
                elif BSAction  == "S ":
                    listb[count].append("普通賣出")
                elif BSAction  == "MB":
                    listb[count].append("融資買入")
                elif BSAction  == "RB":
                    listb[count].append("融資賣出")
                elif BSAction  == "RS":
                    listb[count].append("融券買入")
                elif BSAction  == "MS":
                    listb[count].append("融券賣出")

                listb[count].append(x[x.find("Price")+6:x.find(" Volume")])#委託價
                listb[count].append(x[x.find("Volume")+7:x.find(" BSAction")][:-5])#量/股
                listb[count].append(x[x.find("LogTime")+19:x.find(" LogMsg")][:-3])#成交時間
                #print(listb[count],end='\n\n')
                count+=1;
            i+=1
            return listb
def order(CompCode,buysell):
    url="http://61.220.30.176/weborder/autotrade.asmx/PutOrderXML3?GMRIDStr="+GMRIDStr+"&CompCode="+CompCode+"&Price=1&Volume=1000&BSAction="+buysell+"&OrderType=LMTU&IsOddLot=0&Currency=TWD&OrderNote=ROD&OCType=0&CombineNo=&OrderParameter=0&Lang=TC&str_ip=127.0.0.1"
    #print(url)
    response = requests.get(url)
    root = ET.fromstring(response.text)
    if 'Success' in root.text:   # 使用in運算子檢查
        return('Success')

    elif 'Failure' in root.text:
        return('Failure')


def picture():#表
    start = datetime.datetime(2019, 1, 9)

    end = datetime.datetime(2020, 12, 9)

    df_2330 = web.DataReader('^TWII', 'yahoo',start,end)
    #df_2330 = web.DataReader(['^TWII'], 'yahoo', start, end)

    #df_2330 = web.DataReader(['aapl', 'msft'], 'yahoo', start, end)

    df0 = df_2330['Close'].index
    df1 = df_2330['Open']
    df2 = df_2330['High']
    df3 = df_2330['Low']
    df4 = df_2330['Close']
    df5 = df_2330['Volume']
    avg5=df_2330['Adj Close'].rolling(window=5).mean()
    avg10=df_2330['Adj Close'].rolling(window=10).mean()
    avg20=df_2330['Adj Close'].rolling(window=20).mean()

    a = []

    for s,t,u,v,w,x,i,j,k,l in zip(df0,df1,df2,df3,df4,df5,range(len(df0)),avg5,avg10,avg20):
        a.append([])
        if str(s)[5:6] == '0':
            if int(str(s)[6:7])-1 == 0:
                a[i].append(int(str(s)[0:4])-1)
                a[i].append(12)
            else:
                a[i].append(str(s)[0:4])
                a[i].append(int(str(s)[6:7])-1)
        else:
            a[i].append(str(s)[0:4])
            a[i].append(int(str(s)[5:7])-1)
        if str(s)[8:10] == '0':
            a[i].append(str(s)[9:10])
        else:
            a[i].append(str(s)[8:10])
        a[i].append(round(t, 2))
        a[i].append(round(u, 2))
        a[i].append(round(v, 2))
        a[i].append(round(w, 2))
        a[i].append(round(x, 2))
        if math.isnan(j):
            a[i].append(0)
        else:
            a[i].append(j)
        if math.isnan(k):
            a[i].append(0)
        else:
            a[i].append(k)
        if math.isnan(l):
            a[i].append(0)
        else:
            a[i].append(l)
    return a

def transform_date(date):#TWII()使用
    y, m, d = date.split('/')
    return str(int(y)+1911) + '-' + m  + '-' + d
def TWII():#大盤
    url='https://www.twse.com.tw/exchangeReport/FMTQIK?response=json&date=20200701&'
    res=requests.get(url)
    s=json.loads(res.text)

    nowtime=datetime.datetime.now().strftime("%H:%M")
    updatetime=datetime.time(13, 40, 41)
    utime=updatetime.strftime("%H:%M")

    nowtime=nowtime.replace(":","")
    utime=utime.replace(":","")
    day=datetime.date.today().weekday()
    if(day!=5 and day!=6):
        if(nowtime > utime):
            today=datetime.date.today()
        else:
            if(day==0):
                today=datetime.date.today() - datetime.timedelta(days=3)
            else:
                today=datetime.date.today() - datetime.timedelta(days=1)
    else:
        if(day==5):
            today=datetime.date.today() - datetime.timedelta(days=1)
        else:
            today=datetime.date.today() - datetime.timedelta(days=2)

    for data in (s['data']):
       if((transform_date(data[0])) == str(today)):
           tv=data[1]
           to=data[2].replace(',','')
           taiex=data[4].replace(',','')
           pricing=data[5]

    tv=tv[:-4]
    to=to[:-6]
    to=str(float(to)/100)
    return [round(float(taiex),2),round(float(pricing),2),to,tv]
