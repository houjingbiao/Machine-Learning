# -*- coding: cp936 -*-
import os
os.chdir('D:\\Machine-Learning\\trunk\\programming-collective-intelligence\\chapter03-discovering-groups\\clustering\\clustering')

import clusters

blognames, words, data = clusters.readfile('blogdata.txt')
clust=clusters.hcluster(data)
#clusters.printclust(clust, labels=blognames)

#reload(clusters)
clusters.drawdendrogram(clust, blognames, jpeg='blogclust.jpg')
print 'hello world'