## algo-in-python-without-db-

# 1 - Long Term 
## watch on wkole market stock
## monthly_signal == "BUY_SIGNAL"
### buy @ daily (Short Term) or weekly (Long Term)

# 2- Short Term
## upto 2000 stock in watchlist
## monthly_signal == "BUY_SIGNAL" (NIFTY)
## monthly_signal == "BUY_SIGNAL"
## weekly_signal == "BUY_SIGNAL"
### buy @ 60min (Swing) or daily (Short Term)



# 3- Swing Trade
## upto 500 stock in watchlist
## weekly_signal == "BUY_SIGNAL" (NIFTY)
## weekly_signal == "BUY_SIGNAL"
## daily_signal == "BUY_SIGNAL"
### buy @ 15min (BTST) or  60min (Swing)


# 4- BTST
## upto 200 stock in watchlist
## daily_signal == "BUY_SIGNAL" (NIFTY)
## daily_signal == "BUY_SIGNAL"
## 60min_signal == "BUY_SIGNAL"
### buy @ 5min (intraday) or 15min (BTST)




# 5- Intraday
## upto 50 stock in watchlist
## daily_signal == "BUY_SIGNAL" (NIFTY)
## daily_signal == "BUY_SIGNAL"
## 60min_signal == "BUY_SIGNAL" (NIFTY)
## 60min_signal == "BUY_SIGNAL"
## 15min_signal == "BUY_SIGNAL"
### buy @ 1min (scalping) or  5min (intraday)


# Time Frame and Trading Methods
### montlhy
### weekly (Long Term)
### daily (Short Term)
### 60min (Swing)
### 15min (BTST)
### 5min (intraday)
### 1min (scalping)



# Trend and signal
## A
#### sma_trend ="UP"(1)  or "DOWN"(-1) or "SW"(0)
#### sma_signal ="BUY_SIGNAL"(1) or "SELL_SIGNAL"(-1) or ""(0)
## B
#### range_trend ="UP"(1)  or "DOWN"(-1) or "SW"(0)
#### range_signal ="BUY_SIGNAL"(1) or "SELL_SIGNAL"(-1) or ""(0)
## C
#### linear_reg_trend ="UP"(1)  or "DOWN"(-1) or "SW"(0)
#### linear_reg_signal ="BUY_SIGNAL"(1) or "SELL_SIGNAL"(-1) or ""(0)
## Final
### trend = A + B + C
#### signal = A + B + C
#### +ve = "UP" or "BUY_SIGNAL"
#### -ve = "DOWN" or "SELL_SIGNAL"
#### 0 = "SW" or ""



# Range - 10
#### monthly - 50%
#### weekly - 25%
#### daily - 5%
#### 60min - 2%
#### 15min - 1%
#### 5min - 0.5%
#### 1min - 0.2%

# Range - 5
#### monthly - 25%
#### weekly - 12%
#### daily - 2%
#### 60min - 1%
#### 15min - 0.5%
#### 5min - 0.2%
#### 1min - 0.1%