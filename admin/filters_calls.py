# signals -> filter -> calls
#./data/signals/*  -->  ./data/filters/* --> ./data/calls/*
import json
from time import sleep
from datetime import datetime


def filters(higher_time_frame_file,lower_time_frame_file):
    unconf_buy_list = []
    unconf_sell_list = []
    conf_buy_list =[]
    conf_sell_list = []

    # daystocks = json.loads(jsdaydata)
    with open(higher_time_frame_file,'r') as dayJsonFile:
        daystocks = json.load(dayJsonFile)
    # hourstocks = json.loads(jshourdata)
    with open(lower_time_frame_file,'r') as hourJsonFile:
        hourstocks = json.load(hourJsonFile)

    for stock in daystocks['NSE']:
        # print(daystocks['NSE'][stock]['SMA']['sma50'])
        token = daystocks['NSE'][stock]['token']
    
        # print('-'*50)

        stocksignals = {}
        stocksignals['symbol']=stock
        stocksignals['token'] = token


        if daystocks['NSE'][stock]['SMA']['sma50'] == 'BUY_SIGNAL':
            if hourstocks['NSE'][stock]['SMA']['sma50'] == 'BUY_SIGNAL':
                conf_buy_list.append(stocksignals)
                stocksignals['timestamp-higher'] = daystocks['NSE'][stock]['timestamp']
                stocksignals['timestamp-lower'] = hourstocks['NSE'][stock]['timestamp']
            elif hourstocks['NSE'][stock]['SMA']['sma50'] == '':
                unconf_buy_list.append(stocksignals)
                stocksignals['timestamp-higher'] = daystocks['NSE'][stock]['timestamp']
                stocksignals['timestamp-lower'] = hourstocks['NSE'][stock]['timestamp']

        elif daystocks['NSE'][stock]['SMA']['sma50'] == 'SELL_SIGNAL':
            if hourstocks['NSE'][stock]['SMA']['sma50'] == 'SELL_SIGNAL':
                conf_sell_list.append(stocksignals)
                stocksignals['timestamp-higher'] = daystocks['NSE'][stock]['timestamp']
                stocksignals['timestamp-lower'] = hourstocks['NSE'][stock]['timestamp']
            elif hourstocks['NSE'][stock]['SMA']['sma50'] == '':
                unconf_sell_list.append(stocksignals)
                stocksignals['timestamp-higher'] = daystocks['NSE'][stock]['timestamp']
                stocksignals['timestamp-lower'] = hourstocks['NSE'][stock]['timestamp']

    unconf_dict ={}
    unconf_dict['BUY'] = unconf_buy_list
    unconf_dict['SELL'] = unconf_sell_list

    conf_dict ={}
    conf_dict['BUY'] = conf_buy_list
    conf_dict['SELL'] = conf_sell_list

    signal_dict ={}
    signal_dict['unconfirmed'] =unconf_dict
    signal_dict['confirmed'] = conf_dict

    final_signal ={}
    final_signal['NSE'] =signal_dict

    return final_signal



def calls_generator(filter_json_file,signals_json_file):
    
    with open(filter_json_file,'r') as filterfile:
        btst_dict = json.load(filterfile)

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

    unconf_min15_dict ={}
    unconf_min15_dict['BUY'] = unconf_15min_buy_list
    unconf_min15_dict['SELL'] = unconf_15min_sell_list

    conf_min15_dict ={}
    conf_min15_dict['BUY'] = conf_15min_buy_list
    conf_min15_dict['SELL'] = conf_15min_sell_list

    conf_unconf_dict ={}
    conf_unconf_dict['confirmed'] = conf_min15_dict
    conf_unconf_dict['unconfirmed'] = unconf_min15_dict

    signals_dict ={}
    signals_dict['NSE'] = conf_unconf_dict

    print('$'*50,datetime.now())
    print(signals_dict)

    return signals_dict



till  = datetime(datetime.now().year,datetime.now().month,datetime.now().day,18,15,20)
now = datetime.now()
while (now < till):
    now = datetime.now()

    # filters
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    print("filters : btst is running.......",datetime.now())
    btst_filter_json = filters('./data/signals/day.json','./data/signals/hour.json')
    with open('./data/filters/btst.json','w') as wfp:
        json.dump(btst_filter_json ,wfp)

    print('filters : intraday is running ....',datetime.now())
    intraday_filter_json = filters('./data/signals/hour.json','./data/signals/15min.json')
    with open('./data/filters/intraday.json','w') as wfp:
        json.dump(intraday_filter_json ,wfp)
    



    # calls
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # btst_5min.json
    print('calls : btst_5min is running .......')
    btst_5min = calls_generator('./data/filter/btst.json','./data/signals/5min.json')
    with open('./data/calls/btst_5min.json','w') as btst_5minfile:
        json.dump(btst_5min,btst_5minfile)


    #btst_15min.json
    print('btst_15min is running .......')
    btst_15min = calls_generator('./data/filter/btst.json','./data/signals/15min.json')
    with open('./data/calls/btst_15min.json','w') as btst_15minfile:
        json.dump(btst_15min,btst_15minfile)

    # intraday_1min.json
    print('intraday_1min is running .......')
    intraday_1min = calls_generator('./data/filter/intraday.json','./data/signals/1min.json')
    with open('./data/calls/intraday_1min.json','w') as intraday_1minfile:
        json.dump(intraday_1min,intraday_1minfile)

    # intraday_5min.json
    print('intraday_5min is running .......')
    intraday_5min = calls_generator('./data/filter/intraday.json','./data/signals/5min.json')
    with open('./data/calls/intraday_5min.json','w') as intraday_5minfile:
        json.dump(intraday_5min,intraday_5minfile)
  

    sleep(20)


