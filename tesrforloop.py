# -*- coding: utf-8 -*-
"""
14102016-2.dat
"""


data = [0.1, 0.01, -0.02,4.7,5.3,6]
#print x
print type(data)
for i in data:
    if -1<i<1:
        i = 0
        print i
    elif -4<i<6:
        i = 5
        print i
    else:
        print "error"
