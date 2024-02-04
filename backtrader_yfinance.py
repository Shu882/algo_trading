from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
from datetime import datetime
from strategies import (TestStrategy, TestStrategy2)
import yfinance as yf

cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy2)

ticker = "NVDA"
start='2013-01-01'
end='2022-12-31'
yf_data = yf.download(ticker, start=start, end=end)
data = bt.feeds.PandasData(dataname=yf_data)
# Add the Data Feed to Cerebro
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
