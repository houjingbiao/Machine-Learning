# -*- coding: cp936 -*-
import os
os.chdir('D:\\recommendation\\recommendation\\recommendation')
import data
import recommendation
import xlrd

sheet=xlrd.open_workbook("d:\\recommendation\\recommendation\\recommendation\\ratings.xls").sheet_by_index(0)

#print recommendation.sim_distance(data.critics, '1962', '2321')
#print recommendation.sim_pearson(data.critics, '1962', '2321')
#print recommendation.sim_tanimoto(data.critics, '1962', '2321')

#print recommendation.sim_distance(data.critics, '16', '14')
#print recommendation.sim_pearson(data.critics, '16', '14')
#print recommendation.sim_tanimoto(data.critics, '16', '14')

#print recommendation.topMatches(data.critics, '16', 10, recommendation.sim_distance)
#print recommendation.topMatches(data.critics, '16', 10, recommendation.sim_pearson)
#print recommendation.topMatches(data.critics, '16', 10, recommendation.sim_tanimoto)

#critics_user = data.buildCritics_user(sheet);
#print recommendation.getRecommendation(critics_user, '16')

critics_item = data.buildCritics_item(sheet);
print recommendation.getRecommendationItems(critics_item, recommendation.Matches(critics_item, '16'), '16')
print "hello world"