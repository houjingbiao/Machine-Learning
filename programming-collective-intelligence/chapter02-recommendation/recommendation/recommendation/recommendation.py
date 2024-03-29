# -*- coding: cp936 -*-
from math import sqrt

def sim_distance(prefs, person1, person2):
	#get shared_items
	si={}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
			
	#return 0 when they don't share any item
	if len(si)==0: return 0
	
	sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item], 2)
                        for item in si])
	return float(1.0/(1.0+sqrt(sum_of_squares)))


def sim_pearson(prefs, person1, person2):
    #get shared_items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    #return 0 when they don't share any item
    n = len(si)
    if n==0: return 0

    #sum of all prefs
    sum1=sum([prefs[person1][it] for it in si])
    sum2=sum([prefs[person2][it] for it in si])

    #sum of squres
    sum1Sq=sum([pow(prefs[person1][it], 2) for it in si])
    sum2Sq=sum([pow(prefs[person2][it], 2) for it in si])

    #sum of product
    pSum=sum([prefs[person1][it]*prefs[person2][it] for it in si])

    #calculate pearson value
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den == 0: return 0

    r = num/den
    if r > 1.0: r = 1.0
    return r

def sim_tanimoto(prefs, person1, person2):
    #get shared_items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    #return 0 when they don't share any item
    n = len(si)
    return float(n)/float((len(prefs[person1])+len(prefs[person2])-n))

def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores=[(similarity(prefs, person, other), other) for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def Matches(prefs, person, n=5, similarity=sim_pearson):
    scores=[(similarity(prefs, person, other), other) for other in prefs if other!=person]
    scores.sort()
    scores.reverse()
    return scores

def getRecommendation(prefs, person, similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        if other == person: continue
        sim = similarity(prefs, person, other)

        if sim <= 0: continue
        
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item, 0)
                totals[item]+=prefs[other][item]*sim
                simSums.setdefault(item, 0)
                simSums[item]+=sim
    
    #build a normalized list
    rankings = [(total/simSums[item], item) for item, total in totals.items()]

    rankings.sort()
    rankings.reverse()
    return rankings

def getRecommendationItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}
    for (item, rating) in userRatings.items():
        for(similarity, item2) in itemMatch[item]:
            if item2 in userRatings: continue

            scores.setdefault(item2, 0)
            scores[item2]+=similarity * rating
            
            totalSim.setdefault(item2, 0)
            totalSim[item2]+=similarity
    rankings = [(score/totalSim[item], item) for item, score in scores.items()]

    rankings.sort()
    rankings.reverse()
    return rankings