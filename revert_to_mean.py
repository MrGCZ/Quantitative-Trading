import pandas as pd
import numpy as np
from abupy import ABuSymbolPd
import matplotlib.pyplot as plt


kl_pd=ABuSymbolPd.make_kl_df('usTSLA',n_folds=2)
train_kl=kl_pd[200:350]
test_kl=kl_pd[350:]

close_mean=train_kl.close.mean()
close_std=train_kl.close.std()

sell_signal=close_mean+close_std/3
buy_signal=close_mean-close_std/3

'''
print sell_signal,buy_signal
test_kl.close.plot()
plt.axhline(buy_signal,color='black',lw=1)
plt.show()

'''


buy_index=test_kl[test_kl['close']<=buy_signal].index
test_kl.loc[buy_index,'signal']=1

sell_index=test_kl[test_kl['close']>=sell_signal].index
test_kl.loc[sell_index,'signal']=0

test_kl['keep']=test_kl['signal']
test_kl['keep'].fillna(method='ffill',inplace=True)
test_kl['benchmark_profit']=np.log(test_kl['close']/test_kl['close'].shift(1))

test_kl['trend_profit']=test_kl['keep']*test_kl['benchmark_profit']
#test_kl['trend_profit'].plot()

test_kl[['benchmark_profit','trend_profit']].cumsum().plot(grid=True)

plt.show()66

