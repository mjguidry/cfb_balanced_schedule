# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:51:23 2017

@author: mike
"""

import pandas as pd
import pickle
 
df = pd.read_excel('./Schools_2016.xlsx')
 
print("Column headings:")
print(df.columns)

football_dict=dict()

for index, row in df.iterrows():
    if(row['Sports']=='Football' or row['unitid']==100663):
        name=row['institution_name']
        exp=row['TOTAL_EXPENSE_ALL']
        addr1=row['addr1_txt']
        if(str(addr1)=='nan'):
            addr1=''
        else:
            addr1=addr1+', '
        addr2=row['addr2_txt']
        if(str(addr2)=='nan'):
            addr2=''
        else:
            addr2=addr2+', '
        city=row['city_txt']
        if(str(city)=='nan'):
            city=''
        else:
            city=city+', '
        state=row['state_cd']
        if(str(state)=='nan'):
            state=''
        addr=addr1+addr2+city+state
        football_dict[name]=dict()
        football_dict[name]['exp']=exp
        football_dict[name]['addr']=addr
        football_dict[name]['city']=city+state

football_dict['United States Air Force Academy']={'exp':13024301}
football_dict['United States Air Force Academy']['addr']='2169 Field House Drive, U.S. Air Force Academy, CO' 
football_dict['United States Air Force Academy']['city']='U.S. Air Force Academy, CO'
football_dict['United States Military Academy']={'exp':10068282}
football_dict['United States Military Academy']['addr']='700 Mills Rd, West Point, NY' 
football_dict['United States Military Academy']['city']='West Point, NY'
football_dict['United States Naval Academy']={'exp':10419440}
football_dict['United States Naval Academy']['addr']='121 Blake Rd, Annapolis, MD' 
football_dict['United States Naval Academy']['city']='Annapolis, MD'


#for key, value in sorted(football_dict.items(), key=lambda kv: kv[1]['exp'], reverse=True)[:150]:
#    print key,value

f=open('football_dict.pkl','wb')
pickle.dump(football_dict,f)
f.close()
