# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 10:38:14 2017

@author: MGuidry
"""

import pickle

f=open('dist_matrix.pkl','r')
dist_matrix=pickle.load(f)
f.close()

teams=sorted(dist_matrix)

f=open('metis.txt','wb')
f.write('128 8128 001\r\n')

for team in teams:
    temp_str=''
    for k,opp in enumerate(teams):
        if(opp!=team):
            temp_str+=str(k+1)+' '+str(int(round(dist_matrix[team][opp])))+' '
    temp_str+='\r\n'
    f.write(temp_str)

f.close()
