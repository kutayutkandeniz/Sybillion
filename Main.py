#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 13:20:34 2023

@author: kali
"""

import pandas as pd
import numpy as np

fantom_grant_votes = pd.read_csv(r'/home/kali/Exploratory Data Analysis/fantom unicef/Fantom round/fantom_grant_votes.csv')
print(fantom_grant_votes)


timeaddress = fantom_grant_votes[['created_at', 'source_wallet']].copy()
sourceamount = fantom_grant_votes[['amount','source_wallet']].copy()


""" add 1 seconds column and get seconds froms tring """


timeaddress['seconds'] = pd.DataFrame(fantom_grant_votes['created_at'].str.split().str[1])
timeaddress['seconds'] = pd.DataFrame(fantom_grant_votes['created_at'].str.split(':').str[2])

sourceeamount[]


frequency = timeaddress['seconds'].value_counts()
print(frequency)
      
      




"""
timeframe = pd.DataFrame(fantom_grant_votes['created_at', 'source_wallet'].str.split().str[1])
print(timeframe.loc[:,"created_at"])

"""