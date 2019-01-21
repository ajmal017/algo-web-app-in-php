from datetime  import datetime, timedelta
import pickle, json
from zerodha import Zerodha
import config
from time import sleep


sma_day_pct = config.sma_day_pct
sma_hour_pct = config.sma_hour_pct
sma_15min_pct = config.sma_15min_pct
sma_5min_pct = config.sma_5min_pct
sma_1min_pct = config.sma_1min_pct

sleep_time = config.sleep_time


public_token = config.public_token
access_token = config.access_token
userid = config.userid  

def sma_pct(data):
    l = len(data)
    sum = 0
    for ohlc in data:
        close = ohlc[4]
        sum += close
        sma = sum/l
    sma_pct = (close/sma -1)*100
    return sma_pct,sma

def sma50_pct(data):
    dat = data[-50:]
    return sma_pct(dat)

def sma100_pct(data):
    dat = data[-100:]
    return sma_pct(dat)

def sma200_pct(data):
    dat = data[-200:]
    return sma_pct(dat)

def sma_signal(PRICE_SMA50_pct,PRICE_SMA100_pct,PRICE_SMA200_pct,pct_for_sma):
    signal ={}
    signal['sma50']=""
    signal['sma100'] =""
    signal['sma200']=""
    if (PRICE_SMA50_pct < pct_for_sma) and (PRICE_SMA50_pct >0):
        signal['sma50'] ="BUY_SIGNAL"
    elif (PRICE_SMA50_pct > -pct_for_sma) and (PRICE_SMA50_pct <0):
        signal['sma50'] ="SELL_SIGNAL"
    
    if(PRICE_SMA100_pct < pct_for_sma) and (PRICE_SMA100_pct >0):
        signal['sma100'] ="BUY_SIGNAL"
    elif (PRICE_SMA100_pct > -pct_for_sma) and (PRICE_SMA100_pct <0):
        signal['sma100'] = "SELL_SIGNAL"
    
    if(PRICE_SMA200_pct < pct_for_sma) and (PRICE_SMA200_pct >0):
        signal['sma200'] = "BUY_SIGNAL"
    elif (PRICE_SMA200_pct > -pct_for_sma) and (PRICE_SMA200_pct <0):
        signal['sma200'] ="SELL_SIGNAL"

        # add after commit
    signal['sma_signal'] =''
    if signal['sma50'] == "BUY_SIGNAL":
        if signal['sma100'] != "SELL_SIGNAL":
            if signal['sma200'] !="SELL_SIGNAL":
                signal['sma_signal'] = 'BUY_SIGNAL'
    elif signal['sma50'] == "SELL_SIGNAL":
        if signal['sma100'] != "BUY_SIGNAL":
            if signal['sma200'] != "BUY_SIGNAL":
                signal['sma_signal'] = 'SELL_SIGNAL'
    else:
        if signal['sma100'] == "BUY_SIGNAL":
            if signal['sma200'] !="SELL_SIGNAL":
                signal['sma_signal'] = 'BUY_SIGNAL'
        elif  signal['sma100'] =="SELL_SIGNAL":
            if signal['sma200'] != "BUY_SIGNAL":
                signal['sma_signal'] = 'SELL_SIGNAL'
        else:
            if  signal['sma200'] == "BUY_SIGNAL":
                signal['sma_signal'] = 'BUY_SIGNAL'
            elif signal['sma200'] =="SELL_SIGNAL":
                signal['sma_signal'] = 'SELL_SIGNAL'
            else:
                signal['sma_signal'] = ''

    return signal




def signals(exchange_symbol_token_list,time_frame,from_datetime,pct_for_sma,sleep_time=10):
    signals ={}
    exchange_dict ={}
    for stock in exchange_symbol_token_list:
        exchange,symbol,token = stock
        
        data  = zerodha.get_ohlc(time_frame,token,from_datetime)

        PRICE_SMA50_pct,sma50 = sma50_pct(data)
        PRICE_SMA100_pct,sma100 = sma100_pct(data)
        PRICE_SMA200_pct,sma200 = sma200_pct(data)

        print(symbol,' : sma50 : ',sma50)
        print(symbol,' : sma100 : ',sma100)
        print(symbol,' : sma200 : ',sma200)

        smas_dict = {}
        smas_dict = sma_signal(PRICE_SMA50_pct,PRICE_SMA100_pct,PRICE_SMA200_pct,pct_for_sma)

        symbol_dict = {}
        symbol_dict['SMA'] = smas_dict
        symbol_dict['token'] = token
        symbol_dict['timestamp'] = str(datetime.now())
        exchange_dict[symbol] = symbol_dict
        if exchange == "NSE":
            signals['NSE'] = exchange_dict
        elif exchange == "BSE":
            signals['BSE'] = exchange_dict
        elif exchange == "MCX":
            signals['MCX'] = exchange_dict
        else:
            signals['UNEX'] = exchange_dict
        sleep(sleep_time)

    return signals


zerodha = Zerodha(public_token,access_token,userid)




min = datetime.now().minute
till  = datetime(datetime.now().year,datetime.now().month,datetime.now().day,23,50,20)
now = datetime.now()

loop = 0
while(now < till):
    now = datetime.now()
    loop +=1

    print("loop No : ",loop)
     
    if (loop %7 ==0):
        # weekly 1 times in an hour
        print(" in month",datetime.now())
        sleep(2)
        

    if (loop % 6 ==0):
        print("in week ",datetime.now())




    if (loop % 5 == 0):
        print("  in day",datetime.now())
        from_datetime = str(datetime.today() - timedelta(days=300))[:10]
        with open('./exchange_symbol_token.pkl','rb') as pkfile:
            exchange_symbol_token_list = pickle.load(pkfile)
        signals_dict = signals(exchange_symbol_token_list,"day",from_datetime,sma_day_pct,sleep_time)
        with open('./data/signals/day.json','w') as sigfp:
            json.dump(signals_dict,sigfp)
        sleep(2)
        
    if (loop % 4 ==0):
        print(' in hour',datetime.now())
        from_datetime = str(datetime.today() - timedelta(days=60))[:10]
        with open('./exchange_symbol_token.pkl','rb') as pkfile:
            exchange_symbol_token_list = pickle.load(pkfile)
        signals_dict = signals(exchange_symbol_token_list,"60minute",from_datetime,sma_hour_pct,sleep_time)
        with open('./data/signals/hour.json','w') as sigfp:
            json.dump(signals_dict,sigfp)
        sleep(2)
        
    if (loop % 3 ==0):
        print('in 15min',datetime.now())
        from_datetime = str(datetime.today() - timedelta(days=15))[:10]
        with open('./exchange_symbol_token.pkl','rb') as pkfile:
            exchange_symbol_token_list = pickle.load(pkfile)
        signals_dict = signals(exchange_symbol_token_list,"15minute",from_datetime,sma_15min_pct,sleep_time)
        with open('./data/signals/15min.json','w') as sigfp:
            json.dump(signals_dict,sigfp)
        sleep(2)
        
    if (loop % 2 == 0):
        print('in 5 min',datetime.now())
        from_datetime = str(datetime.today() - timedelta(days=5))[:10]
        with open('./exchange_symbol_token.pkl','rb') as pkfile:
            exchange_symbol_token_list = pickle.load(pkfile)
        signals_dict = signals(exchange_symbol_token_list,"5minute",from_datetime,sma_5min_pct,sleep_time)
        with open('./data/signals/5min.json','w') as sigfp:
            json.dump(signals_dict,sigfp)
        sleep(2)

    if (loop % 1 == 0):
        print('in 1 min',datetime.now())
        if datetime.today().isoweekday == 1:
            from_datetime = str(datetime.today() - timedelta(days=3))[:10]
        else:
            from_datetime = str(datetime.today() - timedelta(days=2))[:10]

        with open('./exchange_symbol_token.pkl','rb') as pkfile:
            exchange_symbol_token_list = pickle.load(pkfile)
        signals_dict = signals(exchange_symbol_token_list,"minute",from_datetime,sma_1min_pct,sleep_time)
        with open('./data/signals/1min.json','w') as sigfp:
            json.dump(signals_dict,sigfp)
        sleep(2)



