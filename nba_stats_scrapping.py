# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 13:19:02 2022

@author: antho
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.basketball-reference.com/players/l/lillada01/gamelog/2021'

data = requests.get(url)
with open("stats/lillard_2021_stats.html","w+", encoding="utf-8")as f:
        f.write(data.text)

with open("stats/lillard_2021_stats.html",encoding="utf-8") as f:
    page = f.read()

soup = BeautifulSoup(page,'lxml')
stats_table = soup.find(id="pgl_basic")
stats_table = pd.read_html(str(stats_table))[0]
stats_table.to_csv(r'./stats/lillard_2021_stats.csv', encoding='utf-8', header='true')
