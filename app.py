#!/usr/bin/env python
# coding: utf-8

# In[1]:


# use python 3.6
import time
import datetime
from datetime import date, timedelta

import os
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dateutil.relativedelta import relativedelta

# from pandas.tseries.offsets import DateOffset
# from pandas.tseries.offsets import MonthOffset

# finnacial data
from nsepy import get_history
from nsepy.derivatives import get_expiry_date


# In[2]:


# get_ipython().system('pip3 install nsepy')


# In[3]:


# path to load and save folders
# create 2 folders - "code" 1 for code and "data_output"
# run notebook from code folder; data will get stored in data_output as csv

cwd = os.getcwd()  # ; print(cwd)
save_path = cwd[:-4]  # ; print(save_path)
print(save_path)


# ### Story so far
#
# * Previously in black swan post we identified that black swan events are more frequent than a normal distribution would lead us to believe
# * We saw the impact of being able to reduce the impact of such events or being able to capture the upside
#
# ### Objective
#
# * There are multiple ways of hedging yourself against such events; which can be another post in itself.
# * For me the most interesting place to start is using equity options.
# * Before we start buying options its always good to backtest different strategies
# * In this post I write about downloading 15 years of options data which can be used in a backtest
#
# Note: All the code is based on the documentation of NSEPY(add link) and the book (add link)

# ### Segue into options 101
#
# * In order to follow further you need to know the basics of options - add youtube video link
# * 2 minute Maggi Noodle version
# 	 * Options are like term insurance - you get a payout if something happens; death in case of term insurance
# 	 * Unlike term insurance - options also have a payout if an event happens
# 	 * Just like term insurance you need to pay a premium
# 	 * Just like term insurance the arrangement is valid for a predefined period
# 	 * Unlike term insurance options work both ways; i.e. depending on how the contract is made options payoff if the value is above or below the contract price
# 	 * Unlike your life insurance these option contracts can also be bought and sold in the markets; changes in their value depends on multiple factors such as time to expiry, market conditions, prevailing interest ratest, difference between the option contract value and current market price
# 			 * Term Insurance Example - You get paid 10 Lakh rupees if you die anytime during the next 15 years; provided you pay us Rs. 75,000 per year
# 			 * Option Contract Example - You get paid a the market price of the NSE Nifty if it closes above 15,000 on the contract expiry date
#
# Note: This is an extremely simplistic view. Please read and watch some videos to understand this further. And don't trade in options till you don't understand the risks

# In[4]:


# lets try to download for a single option first; manually specify dates
sample_opt1 = get_history(
	symbol="NIFTY",
	start=date(2004, 11, 1),
	end=date(2005, 1, 27),
	index=True,
	option_type="PE",
	strike_price=2000,
	expiry_date=date(2005, 1, 27),
)

print(sample_opt1.shape)
sample_opt1.head(n=3)


# ###  As seen above
#
# * Downloading manually is too cumbersome since
# * multiple strikes
# * multiple expiries
# * Limits to 1 contract at a time
# * Add screenshot

# ### Which options data should we download
#
# * Call, Put
# * daily, monthly, yearly
# * monthly - most liquid
# * weekly started around ...
# * 3 months prior to expiry
# * above and below 1000 points
#
# ### So lets code
#
# * if we have to loop we need to automate the changeover of dates and strike prices; lets 1st run a simple code to do that

# In[5]:


# current date - 3 months prior to the 1st option contract expiry
current_date = date(2005, 1, 1)
print(current_date)
print(type(current_date))
type(current_date)


# In[6]:


# price download start date
start_date = current_date + relativedelta(months=-2)
print(start_date)
print(type(start_date))
start_month = current_date.month
print("Start Month:", start_month)

start_yr = start_date.year
print("Start Year: ", start_yr)


# In[7]:


# get expiry date

end_month = current_date.month
print("End Month:", end_month)

end_yr = current_date.year
print("End Year: ", end_yr)

# Use the get expiry function to get a list of expiry dates - sample below
# get_expiry_date returns a list of weekly expiries; use max to get the month end expiry date

expiry_date = max(get_expiry_date(year=end_yr, month=end_month))
print("Expiry_date:", expiry_date, "Type: ", type(expiry_date))
type(expiry_date)


# In[8]:


# test out for a single option - with using dates as variables before we write the loop
sample_opt2 = get_history(
	symbol="NIFTY",
	start=start_date,
	end=expiry_date,
	index=True,
	option_type="PE",
	strike_price=2000,
	expiry_date=expiry_date,
)
print(sample_opt2.shape)
sample_opt2.head(n=3)


# ### Lets loop
#
# * We have to loop over
# 	 * 15 years
# 	 * 12 months in each year
# 	 * At least 6-8 strike prices
# 	 * 2 types of options for each strike
#
# * Also the changeover of dates should be random
# * We need to download data for 3 months prior to each month to the expiry date of the month
# * Start dates have to move in a rolling window
# * Give example

# In[17]:


# define and month year range to loop over
month_list = np.arange(1, 13, step=1)
print(month_list)
yr_list = np.arange(2021, 2022, step=1)
print(yr_list)


# In[10]:


# empty dataframe
nifty_data = pd.DataFrame()  # to use in the loop
option_data = pd.DataFrame()  # to store output


# In[18]:


# break the loop into 2 parts to avoid having to rerun everything if there are querying errors
# for yr in yr_list:
# 	 # loop through all the months and years
# 	 counter = 0
# 	 print('Year: ', yr)
# 	 for mnth in month_list:
# 		 current_dt = date(yr, mnth, 1)
# 		 start_dt = current_dt + relativedelta(months = 0)
# 		 end_dt = max(get_expiry_date(year = yr, month = mnth))

# 		 # print('current: ', current_dt)
# 		 # print('start: ', start_dt)
# 		 # print('end: ', end_dt)

# 		 # get nifty futures data
# 		 nifty_fut = get_history(symbol = 'NIFTY',
# 								start = start_dt, end = end_dt,
# 								index = True,
# 								expiry_date = end_dt)
# 		 nifty_data = nifty_data.append(nifty_fut)

# 		 # calculate high and low values for each month; round off to get strike prices
# 		 high = nifty_fut['Close'].max()
# 		 high = int(round(high/100)*100) + 1000# ; print('High:', high)

# 		 low = nifty_fut['Close'].min()
# 		 low = int(round(low/100)*100) + 1000# ; print('Low :', low)

# 		 for strike in range(low, high, 100): # start, stop, step
# 			 """
# 			 get daily closing nifty index option prices for 3 months
# 			 over the entire range
# 			 """
# 			 # time.sleep(random.randint(10,20)) # pause for random interval so as to not overwhelm the site
# 			 nifty_opt = get_history(symbol = 'NIFTY',
# 									start = start_dt, end = end_dt,
# 									index = True, option_type = 'PE',
# 									strike_price = strike,
# 									expiry_date = end_dt)

# 			 option_data = pd.concat([option_data,nifty_opt])

# 			 #time.sleep(random.randint(20,50)) # pause for random interval so as to not overwhelm the site
# 			 nifty_opt = get_history(symbol = 'NIFTY',
# 									start = start_dt, end = end_dt,
# 									index = True, option_type = 'CE',
# 									strike_price = strike,
# 									expiry_date = end_dt)

# 			 option_data = pd.concat([option_data,nifty_opt])

# 		 counter+=1
# 		 print('Months: ', counter)
# 		 # print(month)


# In[12]:


yr_list = np.arange(2021, 2022, step=1)
print(yr_list)
# yr_list = np.arange(2018, 2021, step = 1 ); print(yr_list)

cepremium = pepremium = 40
cestrikeFound = pestrikeFound = True
profit = 0

# In[19]:


for yr in yr_list:
	counter = 0
	# loop through all the months and years
	print("Year: ", yr)
	for mnth in month_list:
		current_dt = date(yr, mnth, 1)
		start_dt = current_dt + relativedelta(months=0)
		exp_dates = get_expiry_date(year=yr, month=mnth)
		#   end_dt = max(get_expiry_date(year=yr, month=mnth))
		for exp_date in exp_dates:
			try:
				# exp_date = ''
				# first_exp = datetime.datetime.strptime('07/01/2021', "%d/%m/%Y").date()
				# for d in list(exp_dates):
				# 	if d == first_exp:
				# 		exp_date = first_exp
				# 		break
				print(exp_date)
				# print('current: ', current_dt)
				# print('start: ', start_dt)
				# print('sdga')
				# get nifty futures data
				nifty_fut = get_history(
					symbol="BANKNIFTY",
					start=exp_date - timedelta(days=2),
					end=exp_date - timedelta(days=2),
					index=True,
					expiry_date=exp_date,
				)
				nifty_data = nifty_fut
				print(nifty_data)
				# print(nifty_data)
				# calculate high and low values for each month; round off to get strike prices
				# high = nifty_fut["Close"].max()
				# high = int(round(high / 100) * 100) + 1000  # ; print('High:', high)

				# low = nifty_fut["Close"].min()
				# low = int(round(low / 100) * 100) + 1000  # ; print('Low :', low)
				atm = int(round(nifty_fut["Open"] / 100) * 100)

				cestrike = pestrike = atm
				while cestrikeFound:
					nifty_opt = get_history(
						symbol="BANKNIFTY",
						start=exp_date - timedelta(days=2),
						end=exp_date - timedelta(days=2),
						index=True,
						option_type="CE",
						strike_price=cestrike,
						expiry_date=exp_date,
					)
					# print(nifty_opt['Open'][0])
					# print(nifty_opt)
					if (nifty_opt["Open"][0] <= cepremium) and (
						nifty_opt["Open"][0] >= (cepremium - 10)
					):
						cepremium = nifty_opt["Open"][0]
						cestrikeFound = False
					cestrike = cestrike + 100
				while pestrikeFound:
					nifty_opt = get_history(
						symbol="BANKNIFTY",
						start=exp_date - timedelta(days=2),
						end=exp_date - timedelta(days=2),
						index=True,
						option_type="PE",
						strike_price=pestrike,
						expiry_date=exp_date,
					)
					# print(nifty_opt['Open'][0])
					if (nifty_opt["Open"][0] <= pepremium) and (
						nifty_opt["Open"][0] >= (pepremium - 10)
					):
						pepremium = nifty_opt["Open"][0]
						pestrikeFound = False
					pestrike = pestrike - 100
				print(cestrike)
				print(atm)
				print(pestrike)

				nifty_opt = get_history(
					symbol="BANKNIFTY",
					start=exp_date,
					end=exp_date,
					index=True,
					option_type="CE",
					strike_price=cestrike,
					expiry_date=exp_date,
				)
				profit = profit + (cepremium - nifty_opt["Close"][0])
				print(profit)
				nifty_opt = get_history(
					symbol="BANKNIFTY",
					start=exp_date,
					end=exp_date,
					index=True,
					option_type="PE",
					strike_price=pestrike,
					expiry_date=exp_date,
				)
				profit = profit + (pepremium - nifty_opt["Close"][0])
				print(profit)
				# for strike in range(low, high, 100):  # start, stop, step
				# 	"""
				# 	get daily closing nifty index option prices for 3 months
				# 	over the entire range
				# 	"""
				# 	# time.sleep(random.randint(10,20)) # pause for random interval so as to not overwhelm the site
				# 	nifty_opt = get_history(
				# 		symbol="BANKNIFTY",
				# 		start=start_dt,
				# 		end=exp_date,
				# 		index=True,
				# 		option_type="PE",
				# 		strike_price=strike,
				# 		expiry_date=exp_date,
				# 	)

				# 	option_data = pd.concat([option_data, nifty_opt])

				# 	# time.sleep(random.randint(20,50)) # pause for random interval so as to not overwhelm the site
				# 	nifty_opt = get_history(
				# 		symbol="BANKNIFTY",
				# 		start=start_dt,
				# 		end=exp_date,
				# 		index=True,
				# 		option_type="CE",
				# 		strike_price=strike,
				# 		expiry_date=exp_date,
				# 	)

				# 	option_data = pd.concat([option_data, nifty_opt])
				cestrikeFound = pestrikeFound = True
				# time.sleep(60)
				time.sleep(random.randint(10,20)) # pause for random interval so as to not overwhelm the site
			except:
				print("An exception occurred")
				pass
		counter += 1
		print("Months: ", counter)
		# print(month)

# In[21]
# df[df.index.day_name().isin(['Monday','Wednesday','Sunday'])].sort_index(ascending=True).head(5)
option_data.index = pd.to_datetime(option_data.index)
option_data = option_data[option_data.index.day_name().isin(["Thursday"])]


# In[20]:


# visually verify
print(nifty_data.shape)
nifty_data.tail(n=3)


# In[23]:


# visually verify
print(option_data.shape)
option_data.tail(n=3)


# In[16]:


# save to csv for future use
option_data.to_csv(save_path + "data_output/nifty_1 mon_data.csv")
