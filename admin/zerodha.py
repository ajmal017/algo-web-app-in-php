from time import time, strftime
from datetime import datetime, timedelta
import requests, json

def currenttimestamp():
    print(strftime('%X %x %Z'))
    return round(time()*1000)

# https://kitecharts-aws.zerodha.com/api/chart/
# 1270529
# /
# 5minute
# ?public_token=
# nkozx5UiKlto2JU0lLjyxKX0GdcyRxJG
# &user_id=
# ZT8569
# &api_key=kitefront&access_token=
# IlND2uszcyjE27wlrGl3SabmF70qOKc1
# &from=2019-01-04
# &to=
# 2019-01-11
# &ciqrandom=
# 1547207141978

class Zerodha:
    def __init__(self,public_token,access_token,userid):
        self.user_id = userid
        self.url1 = "https://kitecharts-aws.zerodha.com/api/chart/"
        self.token_url2 ="256265"
        self.url3 ="/"
        self.time_frame_url45="60minute"      
        self.url6 ="?public_token="
        self.public_token_url7 =public_token
        self.url8 ="&user_id="
        self.url9 =userid
        self.url10="&api_key=kitefront&access_token="
        self.access_token_url11=access_token
        self.url12="&from="
        self.from_url13="2018-07-15"
        self.url14 ="&to="
        self.to_url15 =str(self.curretdate())[:10]
        self.url16="&ciqrandom="
        self.url17=str(self.currenttimestamp())

    def currenttimestamp(self):
        # print(strftime('%X %x %Z'))
        return str(round(time()*1000))

    def curretdate(self):
        return datetime.today()

    def get_ohlc(self,time_frame,token,from_day):
        self.token_url2 = token
        self.time_frame_url45 = time_frame
        self.from_url13 = from_day
        self.url = self.url1 + self.token_url2 + self.url3 + self.time_frame_url45 + self.url6 + self.public_token_url7 + self.url8 + self.url9 + self.url10 +self.access_token_url11 + self.url12 + self.from_url13 + self.url14 + self.to_url15 + self.url16 + self.url17
        # print(self.url)
        resp = requests.get(self.url)
        data = json.loads(resp.text)
        # print(data)
        if data['status'] == 'success':
            ohlc = data['data']['candles']
            return ohlc
        else:
            print("Error :  No data")

    def place_order(self,exchange,tradingsymbol,transaction_type,order_type,quantity,
        price,product,validity,disclosed_quantity,trigger_price,squareoff,stoploss,trailing_stoploss,variety):
        self.regular_order_url = "https://kite.zerodha.com/api/orders/regular"
        
        datas ={"exchange":exchange,"tradingsymbol":tradingsymbol,"transaction_type":transaction_type,"order_type":order_type,"quantity":quantity,"price":price,"product":product,"validity":validity,"disclosed_quantity":disclosed_quantity,"trigger_price":trigger_price,"squareoff":squareoff,"stoploss":stoploss,"trailing_stoploss":trailing_stoploss,"variety":variety,"user_id":self.user_id}

        resp = requests.post(self.regular_order_url,data=datas)
        print("*"*20)
        print("headers : ",resp.headers)
        print("*"*20)
        print("cookies : ",resp.cookies)
        print("*"*20)
        print("content : ",resp.content)
        print("*"*20)





public_token="XwCqLJAhQXng5pm0u69HVp02cwUbZPCB"
user_id="ZT8569"
access_token="IlND2uszcyjE27wlrGl3SabmF70qOKc1"
token ="1270529"


# curl "https://api.kite.trade/instruments/NSE"  


# zerodha = Zerodha(public_token,access_token,user_id)

# print(zerodha.get_ohlc("5minute",'1270529',5))

# zerodha.place_order("NSE","GAIL","BUY","MARKET",1,0,"CNC","DAY",0,0,0,0,0,"regular")
