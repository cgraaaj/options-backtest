#!/usr/bin/env python
# coding: utf-8

# In[1]:


# use python 3.6
import time
import datetime
from datetime import date, timedelta
import calendar
import os
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dateutil.relativedelta import relativedelta

from nsepy import get_history
from nsepy.derivatives import get_expiry_date

cwd = os.getcwd()  # ; print(cwd)
save_path = cwd[:-4]  # ; print(save_path)
print(save_path)

# define and month year range to loop over
month_list = np.arange(5,6, step=1)
print(month_list)
yr_list = np.arange(2020, 2021, step=1)
print(yr_list)

# empty dataframe
nifty_data = pd.DataFrame()  # to use in the loop
option_data = pd.DataFrame()  # to store output

targetPremium = 40
cestrikeFound = pestrikeFound = True
profit = 0

for yr in yr_list:
	counter = 0
	# loop through all the months and years
	print("Year: ", yr)
	for mnth in month_list:
		current_dt = date(yr, mnth, 1)
		start_dt = current_dt + relativedelta(months=0)
		exp_dates = get_expiry_date(year=yr, month=mnth)
		#   end_dt = max(get_expiry_date(year=yr, month=mnth))
		exp_dates = sorted([x for x in exp_dates if pd.to_datetime(x).day_name() in (["Thursday"])])
		print(exp_dates)
		for exp_date in exp_dates:
			try:
				print(f'---------------Running backtest for the EXPIRY {exp_date}-----------------------------')
				nifty_fut = get_history(
					symbol="BANKNIFTY",
					start=exp_date - timedelta(days=2),
					end=exp_date - timedelta(days=2),
					index=True,
					expiry_date=exp_date,
				)
				nifty_data = nifty_fut
				print(nifty_data)

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
					# nifty_opt.to_csv(save_path + f"data_output/{exp_date}_buy_data.csv")
					if (nifty_opt["Open"][0] <= targetPremium) and (
						nifty_opt["Open"][0] >= (targetPremium - 20)
					):
						sold_cepremium = nifty_opt["Open"][0]
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
					if (nifty_opt["Open"][0] <= targetPremium) and (
						nifty_opt["Open"][0] >= (targetPremium - 20)
					):
						sold_pepremium = nifty_opt["Open"][0]
						pestrikeFound = False
					pestrike = pestrike - 100
				print(f'CE Strike {cestrike}')
				print(f'Underlying Stike {atm}')
				print(f'PE Strike {pestrike}')

				nifty_opt = get_history(
					symbol="BANKNIFTY",
					start=exp_date,
					end=exp_date,
					index=True,
					option_type="CE",
					strike_price=cestrike,
					expiry_date=exp_date,
				)
				# nifty_opt.to_csv(save_path + f"data_output/{exp_date}_data.csv")
				ceProfit = sold_cepremium - nifty_opt["Close"][0]
				print(f"{exp_date}'s CE Payin/Payout {ceProfit}")
				profit = profit + (ceProfit)
				# print(profit)

				nifty_opt = get_history(
					symbol="BANKNIFTY",
					start=exp_date,
					end=exp_date,
					index=True,
					option_type="PE",
					strike_price=pestrike,
					expiry_date=exp_date,
				)
				peProfit = sold_pepremium - nifty_opt["Close"][0]
				print(f"{exp_date}'s PE Payin/Payout {peProfit}")
				profit = profit + (peProfit)
				
				cestrikeFound = pestrikeFound = True
				# time.sleep(60)
				time.sleep(random.randint(10,20)) # pause for random interval so as to not overwhelm the site
			except Exception as e:
				print(f"{e} An exception occurred")
				pass
		counter += 1
		print("Months: ", counter)
		print(f"{calendar.month_name[mnth]} Month's {profit}")
		time.sleep(random.randint(30,60))
print(f'Net profit {profit}')
