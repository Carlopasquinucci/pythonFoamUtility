#!/usr/bin/python

"""
These functions offer easy ways to automate changes in OpenFOAM settings by 
modification of 'constant', 'system', '0' files and other files that define an 
OpenFOAM case.

Run as python boundary_conditions.py

Checked with python3.7
"""

import os
import sys

version=1
subversion=0


if sys.argv[1]=='-help':
	print("Version "+str(version)+"."+str(subversion))
	print("-version for version number")
	print("-help to run the help")
	print("Run as python boundary_conditions.py")

if sys.argv[1]=='-version':
	print("Version "+str(version)+"."+str(subversion))


# constant boundary patch replace
# if name starts with
# in--> patch
# out --> patch
# wall --> wall
# sym --> symmetry



def read_file(file_name):
  with open(file_name) as f:
    content = f.readlines()
  f.close()
  return content


def modify_bc(file_path):
  file_contents = read_file(file_path)
  section_flag = False
  #fil = open("demofile.txt", "w")
  with open(file_path, 'w') as f:
    for line in file_contents:
        #print(str(line))
        if 'inlet' in line:
            section_flag = True
            new_bc="patch"
            
        if 'outlet' in line:
            section_flag = True
            new_bc="patch"
            #
        if ' wall' in line:
            section_flag = True
            new_bc="wall"
           
        if 'symmetry' in line:
            section_flag = True
            new_bc="symmetry"
        if section_flag and "type" in line:
           line = line.replace("patch", new_bc)

        if "}" in line and section_flag == True:
           section_flag = False

        f.write(line)


  f.close()
  return


modify_bc("constant/polyMesh/boundary")
