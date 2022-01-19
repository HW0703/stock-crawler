# -*- coding: utf-8 -*-
"""
Created on Thu May 31 20:39:11 2018

@author: user
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Net_Profit_Margin = pd.read_csv('C:\\Users\\user\\Desktop\\財務\\稅後淨利率.csv',encoding ="utf-8-sig")
Stock_Price = pd.read_csv('C:\\Users\\user\\Desktop\\財務\\年股價.csv',encoding ="utf-8-sig",index_col=0)

df_NPM = Net_Profit_Margin
df_NPM = df_NPM.drop(['代號','名稱','平均淨利(%)'],axis = 1)

dic_NPM = {}
for i in df_NPM:
    dic_NPM[i] = [x for x in df_NPM[i] if not pd.isnull(x)]

dic_25_down = {}
dic_25_50_between = {}
dic_50_75_between = {}
dic_75_up = {}

for i in df_NPM:
    list_25_down = []
    list_25_50_between = []
    list_50_75_between = []
    list_75_up = []
    for j in range (len(df_NPM[i])):
        if df_NPM[i][j] < np.percentile(dic_NPM[i], [25])[0]:
            list_25_down.append(Net_Profit_Margin['代號'][j])
            dic_25_down[i] = list_25_down

        elif df_NPM[i][j] >= np.percentile(dic_NPM[i], [25])[0] and df_NPM[i][j] < np.percentile(dic_NPM[i], [50])[0]:
            list_25_50_between.append(Net_Profit_Margin['代號'][j])
            dic_25_50_between[i] = list_25_50_between

        elif df_NPM[i][j] >= np.percentile(dic_NPM[i], [50])[0] and df_NPM[i][j] < np.percentile(dic_NPM[i], [75])[0]:
            list_50_75_between.append(Net_Profit_Margin['代號'][j])
            dic_50_75_between[i] = list_50_75_between

        elif df_NPM[i][j] > np.percentile(dic_NPM[i], [75])[0]:
            list_75_up.append(Net_Profit_Margin['代號'][j])
            dic_75_up[i] = list_75_up
#==============================================================================

def check_time1 (check_dic):
    check_code_number = []
    for i in sorted(check_dic):
        for j in range (len(check_dic[i])):
            check = 0
            for k in sorted(check_dic):    
                if  check_dic[i][j] in check_dic[k]:
                    check += 1
                else:
                    check += 0
            if check == 13:
                check_code_number.append(check_dic[i][j])
    check_code_number = set(check_code_number)
    check_code_number = list(sorted(check_code_number))
    return check_code_number

def check_time2 (check_dic):
    check_code_number = []
    for i in sorted(check_dic):
        for j in range (len(check_dic[i])):
            check = 0
            for k in sorted(check_dic):    
                if  check_dic[i][j] in check_dic[k]:
                    check += 1
                else:
                    check += 0
            if check >= 12:
                check_code_number.append(check_dic[i][j])
    check_code_number = set(check_code_number)
    check_code_number = list(sorted(check_code_number))
    return check_code_number
    
check_25_down = check_time1 (dic_25_down)
check_25_50_between = check_time2 (dic_25_50_between)
check_50_75_between = check_time1 (dic_50_75_between)
check_75_up = check_time1 (dic_75_up)

#==============================================================================

def price (list_check):
    stock_price = [i for i in Stock_Price[list_check[0]]]
    return stock_price

price_25_down = price(check_25_down)
price_25_50_between = price(check_25_50_between)
price_50_75_between = price(check_50_75_between)
price_75_up = price(check_75_up)

list_x = [i for i in range (len(Stock_Price))]
time = [i for i in Stock_Price.T]
#==============================================================================

plt.plot(list_x, price_25_down, '-o',label=check_25_down[0]+' 25%down') #折線圖 -o點和線 線的標籤
plt.plot(list_x, price_25_50_between, '-o',label=check_25_50_between[0]+' 25%~50%')
plt.plot(list_x, price_50_75_between, '-o',label=check_50_75_between[0]+' 50%~75%')
plt.plot(list_x, price_75_up, '-o',label=check_75_up[0]+' 75%up')
plt.legend(loc='upper left') #顯示標籤在左上角
plt.xticks(list_x,time,rotation = 90,fontsize = 16) #換x軸  rotation=轉換角度
plt.yticks(np.linspace(0,250,26),fontsize = 16)
plt.xlabel('time',fontsize = 20) #x軸標籤
plt.ylabel('price',fontsize = 20) #y軸標籤
plt.gcf().set_size_inches(18, 14) #調圖片size
plt.savefig('稅後淨利率.jpg', dpi=300)
plt.show()
