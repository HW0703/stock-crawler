# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 23:05:01 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

df = pd.read_csv("權益乘數.csv")

data = [] 
for i in df['權益乘數']:
    data.append(float('%.1f' %i))


    
x, y = zip(*Counter(data).items())

list_x = list(x)
list_y = list(y)
for a in range (len(x)):
    list_x[a] = float(list_x[a])
    
new_ticks = np.linspace(1,5,9) #x軸a~b分為幾等分
plt.bar(list_x,list_y,0.07,facecolor="red") #(x,y,圖形大小,圖形顏色)
plt.xlim((1,5)) #x軸個數
plt.xticks(new_ticks)
plt.xlabel('Equity Multiplier') #x軸標籤
plt.ylabel('Company') #y軸標籤
plt.show()
