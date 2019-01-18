import  csv
import pickle



stocks = []
with open('./data/nifty.csv') as csvf:
    csvreader = csv.reader(csvf)
    for data in csvreader:
        symbol = data[0]
        stock = ("NSE",data[0])
        stocks.append(stock)
# print(stocks)


# outfp= open('./zerodhatoken.csv','w')
# with open('./data/kite.csv') as instfp:
#     csvreader = csv.reader(instfp)
#     for data in csvreader:
#         exchange = data[11]
#         symbol = data[2]
#         token = data[0]
#         instrument = ( exchange,symbol ,token)
#         # if instrument == None:
#         #     continue
#         # else:
#             # instruments = instruments.append(instrument)
#         print(instrument)
#         txt  = exchange+','+symbol+','+token+'\n'
#         outfp.writelines(txt)
# outfp.close()


instruments =[]
with open('./zerodhatoken.csv') as csvfp:
    csvreader = csv.reader(csvfp)
    for data in csvreader:
        exchange = data[0]
        symbol = data[1]
        token = data[2]
        instrument = (exchange,symbol,token)
        instruments.append(instrument)
# print(instruments)



exchange_symbol_token = []
for stock in stocks:
    exchange1,symbol1 = stock
    for instrument in instruments:
        exchange2,symbol2, token2 = instrument

        if (exchange1 == exchange2) and (symbol1 == symbol2):
            exchange_symbol_token.append(instrument)
        else:
            continue



# with open('./exchange_symbol_token.pkl','wb') as pkfile:
    # pickle.dump(exchange_symbol_token,pkfile)

