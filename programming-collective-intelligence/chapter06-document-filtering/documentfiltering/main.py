import os
os.chdir('D:\\Machine-Learning\\trunk\\programming-collective-intelligence\\chapter06-document-filtering\\documentfiltering')

import documentfiltering
c1 = documentfiltering.classifier(documentfiltering.getwords)

c1.train('the quick brown jumps over the lazy dog', 'good')
c1.train('make quick mony in the online casino', 'bad')
print c1.fcount('quick', 'good')

print c1.fcount('quick', 'bad')

print('Hello World')