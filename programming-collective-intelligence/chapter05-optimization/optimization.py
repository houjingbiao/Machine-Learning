# -*- coding: cp936 -*-

import time
import random
import math

flights={}
for line in file('schedule.txt'):
    origin, dest, depart, arrive, price = line.strip().split(',')
    flights.setdefault((origin, dest), [])

    flights[(origin, dest)].append((depart, arrive, int(price)))

def getminites(t):
    x = time.strptime(t, '%h:%M')
    return x[3]*60+x[4]