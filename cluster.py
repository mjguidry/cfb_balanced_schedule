# -*- coding: utf-8 -*-
"""
Created on Wed Dec 06 12:47:15 2017

@author: MGuidry
"""

import pickle
from numpy import zeros
from scipy.cluster import hierarchy
from scipy.spatial import distance

f=open('dist_matrix.pkl','r')
dist_matrix=pickle.load(f)
f.close()

teams=sorted(dist_matrix)
dissimilarity=zeros((len(teams),len(teams)))
for row,team in enumerate(teams):
    for col,team2 in enumerate(teams):
        if(team!=team2):
            dissimilarity[row][col]=dist_matrix[team][team2]

dissimilarity = distance.squareform(dissimilarity)
threshold = 0.3
linkage = hierarchy.linkage(dissimilarity, method="complete")
clusters = hierarchy.fcluster(linkage, threshold, criterion="distance")
