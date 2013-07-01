# -*- coding: cp936 -*-
import os
os.chdir('D:\\Machine-Learning\\trunk\\programming-collective-intelligence\\chapter03-discovering-groups\\clustering\\clustering')

import clusters

blognames, words, data = clusters.readfile('blogdata.txt')

#hierarchy clustering
#clust=clusters.hcluster(data)
##clusters.printclust(clust, labels=blognames)
#clusters.drawdendrogram(clust, blognames, jpeg='blogclust.jpg')

#column clustering
#rdata = clusters.rotatematrix(data)
#clust=clusters.hcluster(rdata)
#clusters.drawdendrogram(clust, words, jpeg='wordclust.jpg')

# k-means clustering
#kclust=clusters.kcluster(data, k=10)
#print [blognames[r] for r in kclust[0]]

#zebo.txt
#wants, people, data=clusters.readfile('zebo.txt')
#clust = clusters.hcluster(data, distance = clusters.tanimoto)
#clusters.drawdendrogram(clust, wants, jpeg='zebo_wants_clust.jpg') 

#mds
wants, people, data=clusters.readfile('zebo.txt')
loc = clusters.scaledown(data, wants)
clusters.draw2d(loc, wants)

print 'hello world'