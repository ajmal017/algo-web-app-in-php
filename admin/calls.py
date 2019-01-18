# signals -> filter -> calls

# ./data/filter/* -> ./data/calls/*

# filter -> calls

# btst_json_new = {"NSE": {"unconfirmed": {"BUY": []}, {"SELL": []}, "confirmed": {"BUY": [[{"symbol": "NIFTY 50", "token": "256265"}], [{"symbol": "INFRATEL", "token": "7458561"}], [{"symbol": "DRREDDY", "token": "225537"}], [{"symbol": "HINDPETRO", "token": "359937"}]}, "SELL": [{"symbol": "SUNPHARMA", "token": "857857"}], [{"symbol": "GRASIM", "token": "315393"}], [{"symbol": "IOC", "token": "415745"}]]}}}



from datetime import datetime
from time import sleep
import json



btst_json =""" {"NSE": {"unconfirmed": {"BUY": [], "SELL": []}, "confirmed": {"BUY": [{"symbol": "NIFTY 50", "token": "256265"}, {"symbol": "INFRATEL", "token": "7458561"}, {"symbol": "DRREDDY", "token": "225537"}, {"symbol": "HINDPETRO", "token": "359937"}], "SELL": [{"symbol": "SUNPHARMA", "token": "857857"}, {"symbol": "GRASIM", "token": "315393"}, {"symbol": "IOC", "token": "415745"}]}}}"""

min15_json  = """ {"NSE": {"NIFTY 50": {"SMA": {"sma50": "BUY_SIGNAL", "sma100": "BUY_SIGNAL", "sma200": "BUY_SIGNAL", "sma_signal": "BUY_SIGNAL"}, "token": "256265"}, "INFY": {"SMA": {"sma50": "", "sma100": "", "sma200": "", "sma_signal": ""}, "token": "408065"}}}"""

def calls_generator(filter_json_file,signals_json_file):
    # btst_dict = json.loads(btst_json)
    with open(filter_json_file,'r') as filterfile:
        btst_dict = json.load(filterfile)
    # min15_dict = json.loads(min15_json)
    with open(signals_json_file,'r') as signalfile:
        min15_dict = json.load(signalfile)

    # confirmed
    conf_15min_buy_list =[]
    conf_15min_sell_list =[]
    # unconfirmed
    unconf_15min_buy_list =[]
    unconf_15min_sell_list =[]

    # confirmed_unconfirmed
    for conf_unconf in btst_dict['NSE']:
        # confirmed
        if conf_unconf == 'confirmed':                
            for buy_sell in btst_dict['NSE']['confirmed']:
                if buy_sell == 'BUY':
                    for btst in btst_dict['NSE']['confirmed']['BUY']:
                        symbol = btst['symbol']
                        token = btst['token']

                        min15_signal = min15_dict['NSE'][symbol]['SMA']['sma_signal']
                        min15_token = min15_dict['NSE'][symbol]['token']

                        if token == min15_token:
                            if min15_signal == 'BUY_SIGNAL':
                                symbol_dict = {}
                                symbol_dict['symbol'] = symbol
                                symbol_dict['token'] = token
                                conf_15min_buy_list.append(symbol_dict)
                elif buy_sell == 'SELL':
                    for btst in btst_dict['NSE']['confirmed']['SELL']:
                        symbol = btst['symbol']
                        token = btst['token']

                        min15_signal = min15_dict['NSE'][symbol]['SMA']['sma_signal']
                        min15_token = min15_dict['NSE'][symbol]['token']

                        if token == min15_token:
                            if min15_signal == 'SELL_SIGNAL':
                                symbol_dict = {}
                                symbol_dict['symbol'] = symbol
                                symbol_dict['token'] = token
                                conf_15min_sell_list.append(symbol_dict)
        elif conf_unconf == 'unconfirmed':
            # unconfirmed                    
            for buy_sell in btst_dict['NSE']['unconfirmed']:
                if buy_sell == 'BUY':
                    for btst in btst_dict['NSE']['unconfirmed']['BUY']:
                        symbol = btst['symbol']
                        token = btst['token']

                        min15_signal = min15_dict['NSE'][symbol]['SMA']['sma_signal']
                        min15_token = min15_dict['NSE'][symbol]['token']

                        if token == min15_token:
                            if min15_signal == 'BUY_SIGNAL':
                                symbol_dict = {}
                                symbol_dict['symbol'] = symbol
                                symbol_dict['token'] = token
                                unconf_15min_buy_list.append(symbol_dict)
                elif buy_sell == 'SELL':
                    for btst in btst_dict['NSE']['unconfirmed']['SELL']:
                        symbol = btst['symbol']
                        token = btst['token']

                        min15_signal = min15_dict['NSE'][symbol]['SMA']['sma_signal']
                        min15_token = min15_dict['NSE'][symbol]['token']

                        if token == min15_token:
                            if min15_signal == 'SELL_SIGNAL':
                                symbol_dict = {}
                                symbol_dict['symbol'] = symbol
                                symbol_dict['token'] = token
                                unconf_15min_sell_list.append(symbol_dict)

    print(unconf_15min_buy_list)
    print(unconf_15min_sell_list)
    print(conf_15min_buy_list)
    print(conf_15min_sell_list)

    print('='*50)
    unconf_min15_dict ={}
    unconf_min15_dict['BUY'] = unconf_15min_buy_list
    unconf_min15_dict['SELL'] = unconf_15min_sell_list

    print(unconf_min15_dict)

    conf_min15_dict ={}
    conf_min15_dict['BUY'] = conf_15min_buy_list
    conf_min15_dict['SELL'] = conf_15min_sell_list

    print(conf_min15_dict)

    conf_unconf_dict ={}
    conf_unconf_dict['confirmed'] = conf_min15_dict
    conf_unconf_dict['unconfirmed'] = unconf_min15_dict

    print('%'*50)
    print(conf_unconf_dict)

    signals_dict ={}
    signals_dict['NSE'] = conf_unconf_dict

    print('$'*50)
    print(signals_dict)

    return signals_dict

# # # testing 
# data = calls_generator('./data/filter/btst.json','./data/signals/5min.json')

# # print(data)



till  = datetime(datetime.now().year,datetime.now().month,datetime.now().day,18,15,20)
now = datetime.now()

while (now < till):
    now = datetime.now()

    # ./data/calls/btst_5min.json
    btst_5min = calls_generator('./data/filter/btst.json','./data/signals/5min.json')
    with open('./data/calls/btst_5min.json','w') as btst_5minfile:
        json.dump(btst_5min,btst_5minfile)


    # ./data/calls/btst_15min.json
    btst_15min = calls_generator('./data/filter/btst.json','./data/signals/15min.json')
    with open('./data/calls/btst_15min.json','w') as btst_15minfile:
        json.dump(btst_15min,btst_15minfile)

    # ./data/calls/intraday_1min.json
    intraday_1min = calls_generator('./data/filter/intraday.json','./data/signals/1min.json')
    with open('./data/calls/intraday_1min.json','w') as intraday_1minfile:
        json.dump(intraday_1min,intraday_1minfile)

    # ./data/calls/intraday_5min.json
    intraday_5min = calls_generator('./data/filter/intraday.json','./data/signals/5min.json')
    with open('./data/calls/intraday_5min.json','w') as intraday_5minfile:
        json.dump(intraday_5min,intraday_5minfile)


    # ./data/calls/swingtrade_15min.json


    # ./data/calls/swingtrade_60min.json

    
    sleep(20)


# print(min15_token)
