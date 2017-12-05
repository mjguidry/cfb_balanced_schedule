# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 14:17:00 2017

@author: MGuidry
"""

import pickle
import urllib2, json

f=open('football_dict.pkl','rb')
football_dict=pickle.load(f)
f.close()

f=open('name_map.pkl','rb')
name_map=pickle.load(f)
f.close()

api_key='XX'

url_base='https://maps.googleapis.com/maps/api/geocode/json?&key='+api_key
geo_dict=dict()

for name in name_map:
    ok_flag=0
    addr=football_dict[name]['addr']
    city=football_dict[name]['city']
    url=url_base+'&address='+addr.replace(' ','+')
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    jResponse=json.loads(response.read())
    if(jResponse['status']=='OK'):
        lat=jResponse['results'][0]['geometry']['location']['lat']
        lng=jResponse['results'][0]['geometry']['location']['lng']
        ok_flag=1
    else:
        url=url_base+'&address='+city.replace(' ','+')
        req=urllib2.Request(url)
        response=urllib2.urlopen(req)
        jResponse2=json.loads(response.read())
        if(jResponse2['status']=='OK'):
            lat=jResponse2['results'][0]['geometry']['location']['lat']
            lng=jResponse2['results'][0]['geometry']['location']['lng']
            ok_flag=1
    if(ok_flag==1):
        geo_dict[name]=dict()
        geo_dict[name]['lat']=lat
        geo_dict[name]['lng']=lng
    else:
        print "Fail on "+name

f=open('geo_dict.pkl','wb')
pickle.dump(geo_dict,f)
f.close()
