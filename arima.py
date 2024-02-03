import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf

df = pd.read_csv('./data/附件1-区域15分钟负荷数据.csv', parse_dates=['数据时间'])
df.info()

data = df.copy()
data = data.set_index('数据时间')

plt.plot(data.index, data['总有功功率（kw）'].values)
plt.show()
