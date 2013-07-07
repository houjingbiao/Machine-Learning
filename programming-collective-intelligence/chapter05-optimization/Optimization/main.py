import os
os.chdir("D:\\Machine-Learning\\trunk\\programming-collective-intelligence\\chapter05-optimization\\Optimization")


import Optimization

domain=[(0,9)]*(len(Optimization.people)*2)

print '------random------'
s = Optimization.randomoptimize(domain, Optimization.schedulecost)
Optimization.printschedule(s)

print '------hillclimb------'
s = Optimization.hillclimb(domain, Optimization.schedulecost)
Optimization.printschedule(s)

print '------annealing------'
s = Optimization.annealingoptimize(domain, Optimization.schedulecost)
Optimization.printschedule(s)

print 'Hello world!'