

#import urllib2
#c=urllib2.urlopen('http://kiwitobes.com/wiki/Programming_language.html')
#contents=c.read()
#print contents[0:50]

import os
os.chdir("D:\\Machine-Learning\\trunk\\programming-collective-intelligence\\chapter04-search-and-ranking\\searchengine")
import searchengine

#pagelist=['http://kiwitobes.com/wiki/Perl.html']
#crawler=searchengine.crawler('mydb.db')
#crawler.crawl(pagelist)

#crawler.createindextables()

crawler=searchengine.crawler('searchindex.db')
#crawler.createindextables()
#pages=['http://kiwitobes.com/wiki/Categorical_list_of_programming_languages.html']
#crawler.crawl(pages)


#crawler.calculatepagerank()

#search
#e=searchengine.searcher('searchindex.db')
#e.query('function programming')

import nn

mynn = nn.searchnet('nndb.db')
#mynn.maketables()
kaka1 = mynn.getstrength(0,5,0)
kaka1 = mynn.getstrength(0,5,1)

mynn.setstrength(0,5,0,3)
mynn.setstrength(0,5,1,2)


kaka1 = mynn.getstrength(0,5,0)
kaka1 = mynn.getstrength(0,5,1)


print('Hello World')
