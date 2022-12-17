#!/usr/bin/env python
# coding: utf-8

# In[1]:


# use python 3.6
import csv
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

def getCEPremium(exp_date,cestrike):
	sold_cepremium = 0
	cestrikeFound = True
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
		if not nifty_opt.empty:
			if (nifty_opt["Open"][0] <= targetPremium) and (
				nifty_opt["Open"][0] >= (targetPremium - 20)
			):
				cestrikeFound = False
				sold_cepremium = nifty_opt["Open"][0]
		elif nifty_opt.empty:
			cestrikeFound = False
		else:
			cestrikeFound = True
		cestrike = cestrike + 100
	return {'strike':cestrike,'premium':sold_cepremium}

def getPEPremium(exp_date,pestrike):
	sold_pepremium = 0
	pestrikeFound = True
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
		if not nifty_opt.empty:
			if (nifty_opt["Open"][0] <= targetPremium) and (
				nifty_opt["Open"][0] >= (targetPremium - 20)
			):
				pestrikeFound = False
				sold_pepremium = nifty_opt["Open"][0]
		elif nifty_opt.empty:
			pestrikeFound = False
		else:
			pestrikeFound = True
		pestrike = pestrike - 100
	return {'strike':pestrike,'premium':sold_pepremium}

cwd = os.getcwd()  # ; print(cwd)
save_path = cwd[:-4]  # ; print(save_path)
print(save_path)

# define and month year range to loop over
month_list = np.arange(1,13, step=1)
print(month_list)
yr_list = np.arange(2018, 2019, step=1)
print(yr_list)

# empty dataframe
nifty_data = pd.DataFrame()  # to use in the loop
option_data = pd.DataFrame()  # to store output

targetPremium = 50
cestrikeFound = pestrikeFound = True
profit = 0

trades = []


for yr in yr_list:
	counter = 0
	# loop through all the months and years
	print("Year: ", yr)
	for mnth in month_list:
		current_dt = date(yr, mnth, 1)
		start_dt = current_dt + relativedelta(months=0)
		exp_dates = get_expiry_date(year=yr, month=mnth)
		#   end_dt = max(get_expiry_date(year=yr, month=mnth))
		exp_dates = sorted([x for x in exp_dates if pd.to_datetime(x).day_name() in (["Wednesday","Thursday","Friday"])])
		print(exp_dates)
		for exp_date in exp_dates:
			try:
				print(f'---------------Running backtest for the EXPIRY {exp_date}-----------------------------')
				exp_nifty_fut = get_history(
					symbol="BANKNIFTY",
					start=exp_date - timedelta(days=2),
					end=exp_date - timedelta(days=2),
					index=True,
					expiry_date=exp_date,
				)
				nifty_data = exp_nifty_fut
				print(nifty_data)
				atm = int(round(exp_nifty_fut["Open"] / 100) * 100)
				cestrike = pestrike = atm

				ceData = getCEPremium(exp_date,cestrike)
				print(ceData)
				# while cestrikeFound:
				# 	nifty_opt = get_history(
				# 		symbol="BANKNIFTY",
				# 		start=exp_date - timedelta(days=2),
				# 		end=exp_date - timedelta(days=2),
				# 		index=True,
				# 		option_type="CE",
				# 		strike_price=cestrike,
				# 		expiry_date=exp_date,
				# 	)
				# 	# print(nifty_opt['Open'][0])
				# 	if not nifty_opt.empty:
				# 		if (nifty_opt["Open"][0] <= targetPremium) and (
				# 			nifty_opt["Open"][0] >= (targetPremium - 20)
				# 		):
				# 			cestrikeFound = False
				# 			sold_cepremium = nifty_opt["Open"][0]
				# 	elif nifty_opt.empty:
				# 		cestrikeFound = False
				# 	else:
				# 		cestrikeFound = True
				# 	cestrike = cestrike + 100

				peData = getPEPremium(exp_date, pestrike)
				print(peData)
				# while pestrikeFound:
				# 	nifty_opt = get_history(
				# 		symbol="BANKNIFTY",
				# 		start=exp_date - timedelta(days=2),
				# 		end=exp_date - timedelta(days=2),
				# 		index=True,
				# 		option_type="PE",
				# 		strike_price=pestrike,
				# 		expiry_date=exp_date,
				# 	)
				# 	# print(nifty_opt['Open'][0])
				# 	if not nifty_opt.empty:
				# 		if (nifty_opt["Open"][0] <= targetPremium) and (
				# 			nifty_opt["Open"][0] >= (targetPremium - 20)
				# 		):
				# 			pestrikeFound = False
				# 			sold_pepremium = nifty_opt["Open"][0]
				# 	elif nifty_opt.empty:
				# 		pestrikeFound = False
				# 	else:
				# 		pestrikeFound = True
				# 	pestrike = pestrike - 100
					
				print(f"CE Strike {ceData['strike']}")
				print(f'Underlying Stike {atm}')
				print(f"PE Strike {peData['strike']}")

				if(ceData['strike'] != atm):
					nifty_opt = get_history(
						symbol="BANKNIFTY",
						start=exp_date,
						end=exp_date,
						index=True,
						option_type="CE",
						strike_price=ceData['strike'],
						expiry_date=exp_date,
					)
					# nifty_opt.to_csv(save_path + f"data_output/{exp_date}_data.csv")
					ceProfit = ceData['premium'] - nifty_opt["Close"][0]
					print(f"{exp_date}'s CE Payin/Payout {ceProfit}")
					trades.append({'expiry':exp_date,'type':'ce','boughtAt':nifty_opt["Close"][0],'soldAt':ceData['premium'],'pl':ceProfit})
					profit = profit + (ceProfit)

					# print(profit)
				if(peData['strike'] != atm):
					nifty_opt = get_history(
						symbol="BANKNIFTY",
						start=exp_date,
						end=exp_date,
						index=True,
						option_type="PE",
						strike_price=peData['strike'],
						expiry_date=exp_date,
					)
					peProfit = peData['premium'] - nifty_opt["Close"][0]
					print(f"{exp_date}'s PE Payin/Payout {peProfit}")
					trades.append({'expiry':exp_date,'type':'pe','boughtAt':nifty_opt["Close"][0],'soldAt':peData['premium'],'pl':peProfit})
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
print(trades)
print(f'Net profit {profit}')

profitTrades = [trade for trade in trades if trade['pl'] > 0]

lossTrades = [trade for trade in trades if trade['pl'] < 0]

print(profitTrades)
print(lossTrades)

pkeys = profitTrades[0].keys()
lkeys = lossTrades[0].keys()


with open('Profit2018.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, pkeys)
    dict_writer.writeheader()
    dict_writer.writerows(profitTrades)

with open('Loss2018.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, lkeys)
    dict_writer.writeheader()
    dict_writer.writerows(lossTrades)
