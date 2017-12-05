# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 13:19:18 2017

@author: MGuidry
"""

import urllib2
from bs4 import BeautifulSoup
import pickle

url_base='http://football.stassen.com/cgi-bin/records/all-opp.pl?start=1869&end=2016'
url_base+='&sort=g&mingames=0'

games_dict=dict()

for name in sorted(name_map.keys()):
    if (name!='Coastal Carolina University'):
        team_name=name_map[name]
        games_dict[team_name]=dict()
        url_name=team_name.replace(' ','+')
        url_name=url_name.replace('&','')
        url=url_base+'&team='+url_name
        print url
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)
        table=soup.find('table')
        trs=table.findAll('tr')
        for k in range(2,len(trs)):
            tr=trs[k]
            tds=tr.findAll('td')
            opp=tds[0].getText()
            games=int(tds[4].getText())
            if(opp in name_map.values()):
                games_dict[team_name][opp]=games

for name in name_map:
    team=name_map[name]
    if (team not in games_dict):
        games_dict[team]=dict()
    for opp_name in name_map:
        opp=name_map[opp_name]
        if(opp!=team and opp not in games_dict[team]):
            games_dict[team][opp]=0

f=open('games_dict.pkl','wb')
pickle.dump(games_dict,f)
f.close()
