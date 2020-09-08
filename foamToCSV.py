
#!/usr/bin/python

"""

This function offers an simple way to convert the results file from FOAM format to CSV.
It will erase the strings which start with a word.

How to use it: python foamToCSV.py time/field outputfile.

i.e. python foamToCSV 0/p p

Warning: It works only on reconstructed file

Warning: it will erase also the first numerical line

Warning: it will work only on scalar field. For vector, see foamToCSVVector.py

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
	print("Run as python foamToCSV.py time/field outputfile")
	print("WARNING: It doesn't work with vector fields") 

if sys.argv[1]=='-version':
	print("Version "+str(version)+"."+str(subversion))

def read_file(file_name):
  with open(file_name) as f:
    content = f.readlines()
  f.close()
  return content


def foamToCSV(file_name, filename_out):
  file_contents = read_file(file_name)
  temp = open(filename_out, 'w')
  with open(file_name, 'r') as f:
    flag=False
    for line in file_contents:
	if line[0].isdigit() and flag:
	   	temp.write(line)
		
	if line[0].isdigit():
		flag=True
		
	else:
		flag=False
		

  temp.close()
  f.close()
  return

file_name = sys.argv[1]
filename_out = sys.argv[2]
foamToCSV(file_name, filename_out)
