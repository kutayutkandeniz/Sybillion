#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 12:58:21 2023

@author: kali
"""

import pandas as pd

fantom_grant_votes = pd.read_csv(r'/home/kali/Exploratory Data Analysis/fantom unicef/Fantom round/fantom_grant_votes.csv')
print(fantom_grant_votes)

print(fantom_grant_votes.loc[:,"created_at"])

"""
getting seconds

"""


timeframe = pd.DataFrame(fantom_grant_votes['created_at'].str.split().str[1])
print(timeframe.loc[:,"created_at"])

secondsframe = pd.DataFrame(timeframe['created_at'].str.split(':').str[2])
print(secondsframe.loc[:,"created_at"])




print(secondsframe['created_at'].value_counts())









