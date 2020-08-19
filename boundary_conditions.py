#!/usr/bin/python

"""
These functions offer easy ways to automate changes in OpenFOAM settings by 
modification of 'constant', 'system', '0' files and other files that define an 
OpenFOAM case.
"""

import os
import sys

version=1
subversion=0
"""
if [[ $1 == "-help" ]]; then
	echo "Version $version . $subversion"
	echo "-version for version number"
	echo "-help to run the help"
	echo "-checkMesh to run the checkMesh"
	echo "-checkMesh -parallel nprocessor to run the checkMesh in parallel"
	echo "-verbose to maintain all the log file stored"
exit 1
fi

if [[ $1 == "-version" ]]; then
	echo "Version $version . $subversion"
exit 1
fi
"""
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


#'foo' in '**foo**'


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
            #print(str('inlet')+line)
        if 'outlet' in line:
            section_flag = True
            new_bc="patch"
            #print(str('outlet')+line)
        if ' wall' in line:
            section_flag = True
            new_bc="wall"
            #print(str('wall'))
        if 'symmetry' in line:
            section_flag = True
            new_bc="symmetry"
            print(str('symmetry')+line)
        if section_flag and "type" in line:
           line = line.replace("patch", new_bc)
 #       if section_flag and "physicalType" in line:
 #          line = line.replace("patch", new_bc)
        if "}" in line and section_flag == True:
           section_flag = False
        #fil.write(line)
        f.write(line)

  #fil.close()
  f.close()
  return


modify_bc("constant/polymesh/boundary")
