# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

fantom_grant_votes = pd.read_csv(r'/home/kali/Exploratory Data Analysis/fantom unicef/Fantom round/fantom_grant_votes.csv')
print(fantom_grant_votes)

print(fantom_grant_votes.loc[:,"amount"])

"""
new_df = fantom_grant_votes[['amount','source_wallet']].copy()


filter_ = (new_df['amount'] <= 1)
print(new_df[filter_])

print(new_df['amount'] <= 1)

amounto = 1

lowcount = new_df[new_df <= amounto ].count()
print(lowcount)


"""


"""
amount column
"""



new_df = fantom_grant_votes[['amount','source_wallet']].copy()

amountdf = new_df[['amount']].copy()

filter_ = (amountdf['amount'] <= 1.000)
print(amountdf[filter_])

print(amountdf['amount'] <= 1.000)


amounto = 1.000

lowcount = amountdf[amountdf <= amounto ].count()
print(lowcount)


 





"""

unicef_grant_votes = pd.read_csv(r'/home/kali/Exploratory Data Analysis/fantom unicef/UNICEF round/unicef_grant_votes.csv')


"""