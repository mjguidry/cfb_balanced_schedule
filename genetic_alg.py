# -*- coding: utf-8 -*-
"""
Created on Thu Dec 07 11:40:32 2017

@author: MGuidry
"""

import pickle
import numpy as np
from deap import algorithms, base, creator, tools
import operator
import pylab as plt

def sum_of_costs(x0):
    cost=0
    for c in range(16):
        for t in range(8):
            team=teams[int(x0[8*c+t])]
            for o in range(t,8):
                opp=teams[int(x0[8*c+o])]
                if(team!=opp):
                    cost+=dist_matrix[team][opp]
    return cost

def evaluation(individual):
    return (sum_of_costs(individual),)
    
f=open('dist_matrix.pkl','r')
dist_matrix=pickle.load(f)
f.close()

teams=sorted(dist_matrix)
x0=np.arange(128)
np.random.shuffle(x0)

toolbox = base.Toolbox()
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)
toolbox.register("indices", np.random.permutation, len(teams))
toolbox.register("individual", tools.initIterate, creator.Individual,
                 toolbox.indices)
toolbox.register("population", tools.initRepeat, list, 
                 toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
toolbox.register("evaluate", evaluation)
toolbox.register("select", tools.selTournament, tournsize=3)
pop = toolbox.population(n=100)
fit_stats = tools.Statistics(key=operator.attrgetter("fitness.values"))
fit_stats.register('mean', np.mean)
fit_stats.register('min', np.min)
result, log = algorithms.eaSimple(pop, toolbox,
                             cxpb=0.8, mutpb=0.2,
                             ngen=500, verbose=False,stats=fit_stats)
best_individual = tools.selBest(result, k=1)[0]
print('Fitness of the best individual: ', evaluation(best_individual)[0])                          

for c in range(16):
    print "Conf "+str(c)
    for t in range(8):
        print teams[best_individual[8*c+t]]

plt.figure(figsize=(11, 4))
plots = plt.plot(log.select('min'),'c-', log.select('mean'), 'b-')
plt.legend(plots, ('Minimum fitness', 'Mean fitness'), frameon=True)
plt.ylabel('Fitness'); plt.xlabel('Iterations');

#dissimilarity=zeros((len(teams),len(teams)))
#for row,team in enumerate(teams):
#    for col,team2 in enumerate(teams):
#        if(team!=team2):
#            dissimilarity[row][col]=dist_matrix[team][team2]
#
#vals, vecs = scipy.sparse.linalg.eigsh(dissimilarity, k=16)
#
#for c in range(16):
#    print "Conf "+str(c)
#    for k,vec in enumerate(vecs):
#        if(max(vec)==vec[c]):
#            print teams[k]
#
#X = np.random.rand(128, 16)
#vals,vecs=scipy.sparse.linalg.lobpcg(dissimilarity, X)
#for c in range(16):
#    print "Conf "+str(c)
#    for k,vec in enumerate(vecs):
#        if(max(vec)==vec[c]):
#            print teams[k]