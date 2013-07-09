import os
os.chdir('D:\\Machine-Learning\\trunk\\programming-collective-intelligence\\chapter06-document-filtering\\documentfiltering')

import documentfiltering
#c1 = documentfiltering.naivebayes(documentfiltering.getwords)
c1 = documentfiltering.fisherclassifier(documentfiltering.getwords)
documentfiltering.sampletrain(c1)

print c1.classify('quick rabbit', default='unknown')


print('Hello World')