import pandas as pd
import numpy as np
from abupy import ABuSymbolPd

kl_pd=ABuSymbolPd.make_kl_df('usTSLA',n_folds=2)
train_kl=kl_pd[:252]
test_kl=kl_pd[252:]

close_mean=train_kl.close.mean()
close_std=train_kl.close.std()

sell_signal=close_mean+close_std/3
buy_signal=close_mean-close_std/3

