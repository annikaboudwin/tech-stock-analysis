#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import packages
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime


# Tech stocks: NVIDIA Corporation (NVDA), GameStop Corp. (GME), Tesla, Inc. (TSLA), Nokia Oyj (NOK)

# In[3]:


symbols = ['NVDA', 'GME', 'TSLA', 'NOK']

start_date = datetime(2023, 6, 1)
end_date = datetime(2024, 6, 1)

stock_data = yf.download(symbols, start_date, end_date)
stock_data


# In[5]:


stock_data_closing_prices = stock_data['Adj Close']
stock_data_closing_prices.plot()
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price Over Time')
plt.title('Tech Stocks Adjusted Price')
plt.show()


# In[6]:


stock_data_daily_returns = stock_data['Adj Close'].pct_change()
stock_data_daily_returns.plot()
plt.xlabel('Date')
plt.ylabel('Rate of Return')
plt.title('Daily Simple Rate of Return over Time')
plt.show()


# In[8]:


fig = plt.figure(figsize = (15, 15))
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax1.plot(stock_data['Adj Close']['GME'].pct_change())
ax1.set_title('GameStop')
ax2.plot(stock_data['Adj Close']['NOK'].pct_change())
ax2.set_title('Nokia')
ax3.plot(stock_data['Adj Close']['NVDA'].pct_change())
ax3.set_title('NVIDIA')
ax4.plot(stock_data['Adj Close']['TSLA'].pct_change())
ax4.set_title('Tesla')
plt.tight_layout()
plt.show()


# In[9]:


daily_mean = stock_data_daily_returns.mean()
daily_mean


# In[10]:


daily_mean.keys()


# In[12]:


height = []

for key in daily_mean.keys():
    height.append(daily_mean[key])
height


# In[13]:


x_pos = np.arange(len(daily_mean.keys()))


# In[14]:


plt.bar(x_pos, height)

plt.xticks(x_pos, daily_mean.keys())

plt.xlabel('Tech Stocks')
plt.ylabel('Daily Mean')
plt.title('Daily Mean Rate of Return')
plt.show()


# In[15]:


daily_var = stock_data_daily_returns.var()
daily_var


# In[16]:


daily_var.keys()


# In[17]:


height = []

for key in daily_var.keys():
    height.append(daily_var[key])

height


# In[18]:


x_pos = np.arange(len(daily_var.keys()))

plt.bar(x_pos, height)
plt.xticks(x_pos, daily_var.keys())

plt.xlabel('Tech Stocks')
plt.ylabel('Variance')
plt.title('Daily Variance')
plt.show()


# In[21]:


daily_std = stock_data_daily_returns.std()
daily_std


# In[22]:


daily_std.keys()


# In[23]:


height = []

for key in daily_std.keys():
    height.append(daily_std[key])
    
height


# In[24]:


x_pos = np.arange(len(daily_std.keys()))

plt.bar(x_pos, height)
plt.xticks(x_pos, daily_std.keys())
plt.xlabel('Tech Stocks')
plt.ylabel('Standard Deviation')
plt.title('Daily Standard Deviation')
plt.show()


# In[25]:


print(stock_data_daily_returns.corr())


# In[26]:


daily_cov = stock_data_daily_returns.cov()
daily_cov


# In[33]:


# If there was $5,000 to invest over four portfolios

# Don't invest in Tesla, it has had a negative return over the last year

# $3,500 in NVIDIA, $1,000 in Nokia, $500 in GameStop
expected_return = .7 * .0044 + .2 * 0.0002 + .1 * 0.002
total_std = .7 * 0.028 + .2 * 0.02 + .1 * 0.083
print(expected_return)
print(total_std)


# In[34]:


# If you did invest in Tesla

# $2,500 in NVIDIA, $1,000 in Nokia, $1,000 in Tesla, $500 in GameStop
expected_return = .5 * .0044 + .2 * 0.0002 + .2 * 0.000094 + .1 * 0.002
total_std = .5 * 0.028 + .2 * 0.02 + 0.2 * 0.032 + .1 * 0.083
print(expected_return)
print(total_std)


# In[35]:


# Investing only in NVIDIA

# $5,000 in NVIDIA
expected_return = 1 *.0044
total_std = 1 * 0.028
print(expected_return)
print(total_std)


# In[37]:


# Investing in NVIDIA and Nokia

# $2,500 each
expected_return = .5 * 0.0044 + .5 * 0.0002
total_std = .5 * 0.028 + 0.5 * 0.02
print(expected_return)
print(total_std)


# In[28]:


port_returns = [.0044, .0002, .002]
port_volatility = [0.00077, 0.00038, 0.0069]
stock_weights = [.7, .2, .1]

