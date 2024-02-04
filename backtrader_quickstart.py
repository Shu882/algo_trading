from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import backtrader as bt
import datetime
from strategies import (TestStrategy, TestStrategy2)


cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy2)
# Create a Data Feed
datapath = './orcl-1995-2014.txt'
data = bt.feeds.YahooFinanceCSVData(
    dataname=datapath,
    # Do not pass values before this date
    fromdate=datetime.datetime(2000, 1, 1),
    # Do not pass values before this date
    todate=datetime.datetime(2000, 12, 31),
    # Do not pass values after this date
    reverse=False)

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