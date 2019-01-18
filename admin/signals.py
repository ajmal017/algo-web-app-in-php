# 4- BTST
# upto 200 stock in watchlist
# daily_signal == "BUY_SIGNAL" (NIFTY)
# daily_signal == "BUY_SIGNAL"
# 60min_signal == "BUY_SIGNAL"
# buy @ 5min (intraday) or 15min (BTST)


# Trend and signal
# A
# sma_trend ="UP"(1) or "DOWN"(-1) or "SW"(0)
# sma_signal ="BUY_SIGNAL"(1) or "SELL_SIGNAL"(-1) or ""(0)

# B
# range_trend ="UP"(1) or "DOWN"(-1) or "SW"(0)
# range_signal ="BUY_SIGNAL"(1) or "SELL_SIGNAL"(-1) or ""(0)

# C
# linear_reg_trend ="UP"(1) or "DOWN"(-1) or "SW"(0)
# linear_reg_signal ="BUY_SIGNAL"(1) or "SELL_SIGNAL"(-1) or ""(0)

# Final
# trend = A + B + C
# signal = A + B + C

# +ve = "UP" or "BUY_SIGNAL"

# -ve = "DOWN" or "SELL_SIGNAL"

# 0 = "SW" or ""



### Range - 10
# daily - 5%
# 60min - 2%


### Range - 5
# daily - 2%
# 60min - 1%



#sma 50 or 100 or 200
# monthly 15%
# weekly 10%
# daily 5%
# 60min 2%
# 15min 1%
# 5min 0.5%
# 1min 0.2%
from datetime  import datetime, timedelta
import pickle, json
from zerodha import Zerodha
import config
from time import sleep

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

# only for testing
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
print('in 5 min',datetime.now())
from_datetime = str(datetime.today() - timedelta(days=5))[:10]
with open('./exchange_symbol_token.pkl','rb') as pkfile:
    exchange_symbol_token_list = pickle.load(pkfile)
signals_dict = signals(exchange_symbol_token_list,"5minute",from_datetime,0.5,20)
with open('./data/signals/5min.json','w') as sigfp:
    json.dump(signals_dict,sigfp)
sleep(2)





# for ./data/signals/day.json
from_datetime = str(datetime.today() - timedelta(days=300))[:10]
with open('./exchange_symbol_token.pkl','rb') as pkfile:
    exchange_symbol_token_list = pickle.load(pkfile)
signals_dict = signals(exchange_symbol_token_list,"day",from_datetime,5,10)
with open('./data/signals/day.json','w') as sigfp:
    json.dump(signals_dict,sigfp)
 

# $$$$$$$$$$$$$$$$$$$$$$
if datetime.now() < datetime(datetime.now().year,datetime.now().month,datetime.now().day,7,0,0):
    # run month
    pass
if datetime.now() < datetime(datetime.now().year,datetime.now().month,datetime.now().day,8,0,0):
    # run week
    pass
# if datetime.now() < datetime(datetime.now().year,datetime.now().month,datetime.now().day,9,10,0):
    # run day
    # # for ./data/signals/day.json
    from_datetime = str(datetime.today() - timedelta(days=300))[:10]
    with open('./exchange_symbol_token.pkl','rb') as pkfile:
        exchange_symbol_token_list = pickle.load(pkfile)
    signals_dict = signals(exchange_symbol_token_list,"day",from_datetime,5,10)
    with open('./data/signals/day.json','w') as sigfp:
        json.dump(signals_dict,sigfp)
    




min = datetime.now().minute
till  = datetime(datetime.now().year,datetime.now().month,datetime.now().day,15,50,20)
now = datetime.now()
while(now < till):
    now = datetime.now()
     
    if (min <= 45) and (min >= 60):
        # weekly 1 times in an hour
        print(" in week",datetime.now())
        sleep(2)
        

    if ((min%30) >= 20) and ((min%30) <= 30):
        # day - 2 times in an hour
        # for ./data/signals/day.json
        print("  in day",datetime.now())
        from_datetime = str(datetime.today() - timedelta(days=300))[:10]
        with open('./exchange_symbol_token.pkl','rb') as pkfile:
            exchange_symbol_token_list = pickle.load(pkfile)
        signals_dict = signals(exchange_symbol_token_list,"day",from_datetime,5,10)
        with open('./data/signals/day.json','w') as sigfp:
            json.dump(signals_dict,sigfp)
        sleep(2)
        
    if ((min%20) >= 15) and ((min%20) <= 20):
        # hour - 3 times in hour
        print(' in hour',datetime.now())
        from_datetime = str(datetime.today() - timedelta(days=60))[:10]
        with open('./exchange_symbol_token.pkl','rb') as pkfile:
            exchange_symbol_token_list = pickle.load(pkfile)
        signals_dict = signals(exchange_symbol_token_list,"60minute",from_datetime,2,20)
        with open('./data/signals/hour.json','w') as sigfp:
            json.dump(signals_dict,sigfp)
        sleep(2)
        
    if ((min%10) >= 7) and ((min%10) <= 10):
        # 15min -6 times in an hour
        print('in 15min',datetime.now())
        from_datetime = str(datetime.today() - timedelta(days=15))[:10]
        with open('./exchange_symbol_token.pkl','rb') as pkfile:
            exchange_symbol_token_list = pickle.load(pkfile)
        signals_dict = signals(exchange_symbol_token_list,"15minute",from_datetime,1,20)
        with open('./data/signals/15min.json','w') as sigfp:
            json.dump(signals_dict,sigfp)
        sleep(2)
        
    if ((min%5) >= 3) and ((min%5) <= 5):
        # 5 min - 12 times in ah hour
        print('in 5 min',datetime.now())
        from_datetime = str(datetime.today() - timedelta(days=5))[:10]
        with open('./exchange_symbol_token.pkl','rb') as pkfile:
            exchange_symbol_token_list = pickle.load(pkfile)
        signals_dict = signals(exchange_symbol_token_list,"5minute",from_datetime,0.5,20)
        with open('./data/signals/5min.json','w') as sigfp:
            json.dump(signals_dict,sigfp)
        sleep(2)
    
    
    print('in 1 min',datetime.now())
    if datetime.today().isoweekday == 1:
        from_datetime = str(datetime.today() - timedelta(days=3))[:10]
    else:
        from_datetime = str(datetime.today() - timedelta(days=2))[:10]

    with open('./exchange_symbol_token.pkl','rb') as pkfile:
        exchange_symbol_token_list = pickle.load(pkfile)
    signals_dict = signals(exchange_symbol_token_list,"minute",from_datetime,0.2,20)
    with open('./data/signals/1min.json','w') as sigfp:
        json.dump(signals_dict,sigfp)
    sleep(2)
        #  1 min
        
    min = datetime.now().minute

# in last after market is closed
# month
print('in month',datetime.now())

# week
print(' in week',datetime.now())

# day
print(' in  day',datetime.now())
from_datetime = str(datetime.today() - timedelta(days=300))[:10]
with open('./exchange_symbol_token.pkl','rb') as pkfile:
    exchange_symbol_token_list = pickle.load(pkfile)
signals_dict = signals(exchange_symbol_token_list,"day",from_datetime,5,10)
with open('./data/signals/day.json','w') as sigfp:
    json.dump(signals_dict,sigfp)



