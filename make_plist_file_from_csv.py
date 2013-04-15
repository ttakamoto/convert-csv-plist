import os
import plistlib
import csv
import sys

# Load the .csv file
csvr = csv.reader(open(sys.argv[1], 'rb'), delimiter=',')

# Preparing output file
if not os.path.exists('config_output'):
    os.makedirs('config_output')
outfile = 'config_output/settings.plist';

i = 0

alist = []
blist = {};

for row in csvr:
    # skipping the formatted columns
    if(i>0):
        for col in row:
            alist.append(col)
        try:
            blist[alist[0]]
        except KeyError:
            blist[alist[0]] = None

        # Test whether variable is defined to be None
        if blist[alist[0]] is None:
            blist[alist[0]] =  {};
        blist[alist[0]][alist[1]] = alist[2];
        alist = []
    i+=1

plistlib.writePlist(blist, outfile)