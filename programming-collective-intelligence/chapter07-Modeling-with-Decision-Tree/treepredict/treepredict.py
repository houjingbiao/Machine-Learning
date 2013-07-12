import os
import math
import copy
os.chdir('D:\\Machine-Learning\\trunk\\programming-collective-intelligence\\chapter07-Modeling-with-Decision-Tree\\treepredict')

#training data
class dataType:
    def __init__(self, company, country, hasHouse, age, category):
        self.features = {}
        self.features['company'] = company
        self.features['country'] = country
        self.features['hasHouse'] = hasHouse
        self.features['age'] = age
        self.category = category

def getDataCounts(Data, category):
    return len([oneData for oneData in Data if oneData.category == category])

class TreeNode:
    def __init__(self, feature_domain=None, isLeaf = False, TraingingData = None):
        #self.feature = feature
        self.isLeaf = isLeaf
        self.Data = TraingingData
        self.children = {}
        #self.children = dict(zip(feature_domain, [False]*len(self.Data[0].features)))
        self.epsilon = 0.01
        self.generateTree()
        

    def generateTree(self):
        is_feature_used = dict(zip(self.Data[0].features, [False]*len(self.Data[0].features)))

        #the entropy
        counts = {}
        for onedata in self.Data:
            counts.setdefault(onedata.category, 0.0)
            counts[onedata.category]+=1.0
    
        if len(counts) == 1:
            self.isLeaf = True
            self.category = self.Data[0].category
            return

        totalCount = float(len(self.Data))
        current_entropy = sum([-1 * counts[key] / totalCount * math.log(counts[key] / totalCount) for key in counts])

        #find the best feature used as node
        min_entropy = current_entropy
        bestFeature = None
        for feature in is_feature_used.keys():
            if is_feature_used[feature] == False:
                conditioned_Entropy = get_conditioned_entropy(self.Data, feature)
                if conditioned_Entropy < min_entropy and current_entropy - conditioned_Entropy > self.epsilon:
                    min_entropy = conditioned_Entropy
                    bestFeature = feature

        if bestFeature == None:
            categories = set([onedata.category for onedata in self.Data])
            new_counts = [(getDataCounts(self.Data, category), category) for category in categories]
            new_counts.sort()
            ranked = [v for (s,v) in new_counts]
            self.category = ranked[0]
            self.isLeaf = True
        else:
            #insert a new TreeNode
            self.isLeaf = False
            self.feature = bestFeature
            feature_value_domain = set([line.features[bestFeature] for line in self.Data])
            for feature_val in feature_value_domain:
                newdata = []
                for onedata in self.Data:
                   if onedata.features[bestFeature] == feature_val:
                       temp = copy.deepcopy(onedata)
                       del temp.features[bestFeature]
                       newdata.append(copy.deepcopy(onedata))
                self.children[feature_val] = TreeNode(None, False, newdata)



def get_conditioned_entropy(data, feature):
    counts = {}
    counts2 = {}
    for line in data:
        counts.setdefault((line.features[feature], line.category), 0.0)
        counts[(line.features[feature], line.category)]+=1.0
        counts2.setdefault(line.features[feature], 0.0)
        counts2[line.features[feature]]+=1.0

    totalCount = float(len(data))
    ret = sum([-1*counts[(key1, key2)]/totalCount * math.log(counts[(key1, key2)]/counts2[key1])
                for (key1, key2) in counts])
    return ret