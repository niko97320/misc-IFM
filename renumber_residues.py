#!/usr/bin/env python

import sys

# flblanc ACerdan Sconti Nmartin
# 15 Janvier 2016  
# 13 avril 2015
# GPL

input_filename = str(sys.argv[1])
output_filename= str(sys.argv[2])
# ID of the first residue in the initial PDB. Far later: Implement as a argument
firstRes= 1
# ID of the first Chain in the initial PDB
chainID="A"
resNumber = firstRes
currResNumber = firstRes

with open(input_filename,'r') as input_file:
    with open(output_filename,'w') as output_file:
        for line in input_file:
            # Grab only the line containing ATOM
            if line.startswith("ATOM"):
                # If the chain ID changes restart numbering to firstRes
                if line[21] != chainID :
                    chainID = line[21]
                    resNumber = firstRes
                    currResNumber = int(line[22:26]) 
                oldResNumber = currResNumber
                currResNumber = int(line[22:26])
                # Increment the resnmuber based on if the previous numbering is different
                # from the actual number. Doing so we do not loose the continuous numbering
                # per residue. 
                if oldResNumber != currResNumber :
                    resNumber += 1
                
# Warning. What follows is an example of particularly ugly Python.
# It is basically a workaround to modify a string, going through an 
# intermediate list because strings are not mutable in Python.
                resNumberl = list("%4i" %(resNumber))
                modified_line = list(line)
                modified_line[22:26] = resNumberl
                modified_line = ''.join(modified_line)
                output_file.write(modified_line)
