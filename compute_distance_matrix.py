# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:17:28 2017

@author: mike
"""

import pickle
from math import radians, cos, sin, asin, sqrt

f=open('football_dict.pkl','rb')
g=open('games_dict.pkl','rb')
h=open('geo_dict.pkl','rb')
j=open('name_map.pkl','rb')

football_dict=pickle.load(f)
games_dict=pickle.load(g)
geo_dict=pickle.load(h)
name_map=pickle.load(j)

f.close()
g.close()
h.close()
j.close()


def haversine(team1, team2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    lat1=geo_dict[team1]['lat']    
    lon1=geo_dict[team1]['lng']    
    lat2=geo_dict[team2]['lat']    
    lon2=geo_dict[team2]['lng']    

    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    r = 3956 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

scale_dist1=haversine('University of Miami','University of Washington-Seattle Campus')
max_dist2=max([football_dict[name]['exp'] for name in name_map])
min_dist2=min([football_dict[name]['exp'] for name in name_map])
scale_dist2=max_dist2-min_dist2
scale_dist3=max([max(games_dict[team].values()) for team in games_dict])

dist_matrix=dict()

for name in name_map:
    if(name!='Coastal Carolina University' and name!='University of North Carolina at Charlotte'):
        team=name_map[name]
        dist_matrix[team]=dict()
        for name2 in name_map:
            if(name2!='Coastal Carolina University' and 
                name2!='University of North Carolina at Charlotte' and
                name2!=name):
                team2=name_map[name2]
                dist1=100*haversine(name,name2)/scale_dist1
                dist2=100.*abs(football_dict[name]['exp']-football_dict[name2]['exp'])/scale_dist2
                dist3=100-100.*games_dict[team][team2]/scale_dist3
                dist_matrix[team][team2]=sqrt(dist1**2+dist2**2+dist3**2)

f=open('dist_matrix.pkl','wb')
pickle.dump(dist_matrix,f)
f.close()
