#!/usr/bin/python

"""
This function will calculate some statistics (Average, Max, Min) from a scalar field file, previous cleaned by foamToCSV.py
How to use it: Run as python stat.py time/field

Tested with Python 2.7.16
"""

import os
import sys

version=1
subversion=0


if sys.argv[1]=='-help':
	print("Version "+str(version)+"."+str(subversion))
	print("-version for version number")
	print("-help to run the help")
	print("python stat.py time/field")
	print("WARNING: It doesn't work with vector fields") 

if sys.argv[1]=='-version':
	print("Version "+str(version)+"."+str(subversion))


import numpy as np
print('Opening file - It would take some time')
x = np.loadtxt("Ma")

print('Statistical value under evaluation')
print('Total:', np.sum(x))
print('Average:', np.average(x))
print('Max:', np.amax(x))
print('Min:', np.amin(x))
