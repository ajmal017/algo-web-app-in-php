
# data/signals/day.json
# signals -> filter
# data/filter/btst.jsoon


import json
from time import sleep


# with open('./data/signals/day.json','r') as dayJsonFile:
    # data = json.load(dayJsonFile)



# print(daystocks['NSE'])
# print('*'*50)

def filter(higher_time_frame_file,lower_time_frame_file):
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

# final_signal = filter('./data/signals/day.json','./data/signals/day.json')
# print(final_signal)

while True:
    btst_filter_json = filter('./data/signals/day.json','./data/signals/hour.json')
    with open('./data/filter/btst.json','w') as wfp:
        json.dump(btst_filter_json ,wfp)

    intraday_filter_json = filter('./data/signals/hour.json','./data/signals/15min.json')
    with open('./data/filter/intraday.json','w') as wfp:
        json.dump(intraday_filter_json ,wfp)
  


    sleep(20)

