# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 02:41:40 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

df = pd.read_csv("稅後淨利率.csv")

data = [] 
for i in df['平均淨利(%)']:
    data.append(float('%.1f' %i))
    
x, y = zip(*Counter(data).items())

list_x = list(x)
list_y = list(y)
for a in range (len(x)):
    list_x[a] = float(list_x[a])
    
new_ticks = np.linspace(-10,10,21) #x軸a~b分為幾等分
#plt.plot(x, y, '-o') # 點和線
plt.bar(list_x,list_y,0.07,facecolor="red") #(x,y,圖形大小,圖形顏色)
plt.xlim((-10,10)) #x軸個數(a,b)
plt.xticks(new_ticks)
plt.xlabel('Net Profit Margin (%)') #x軸標籤
plt.ylabel('Company') #y軸標籤
plt.show()


