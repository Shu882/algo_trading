from datetime import datetime, date
import backtrader as bt
import pandas as pd
from ib_insync import *
from Learning.algo_trading_components.Backtesting.backtrader.strategies import TestStrategy, TestStrategy2

ib = IB()
# util.startLoop()  # uncomment this line when in a notebook
ib.connect('127.0.0.1', 7497, clientId=29)
print(ib.isConnected())
contract = Stock('NVDA', 'SMART', 'USD')
bars = ib.reqHistoricalData(
    contract, endDateTime=datetime(2024, 1, 1), durationStr='10 Y',
    barSizeSetting='1 day', whatToShow='TRADES', useRTH=True)

# convert to pandas dataframe (pandas needs to be installed):
df = util.df(bars)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy2)
data = bt.feeds.PandasData(dataname=df)
cerebro.adddata(data)
cerebro.broker.setcash(100000.0)
# Add a FixedSize sizer according to the stake
cerebro.addsizer(bt.sizers.FixedSize, stake=1000)
# 0.1% ... divide by 100 to remove the %
cerebro.broker.setcommission(commission=0.001)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot()
