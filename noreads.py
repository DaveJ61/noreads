#!/usr/bin/env python

from __future__ import division
import re, sys, csv, math, time
from itertools import (takewhile,repeat, islice)
import timeit

start = timeit.default_timer()

#inputfile = "TOTE-CNV1-20160325-LINK1.log" 
inputfile = "TOTE-CNV1.log" 

def main():
    count = 0

    linecount = rawbigcount(inputfile)
    print "Number of lines in file: %d" %linecount
    print "Python version: %d.%d" % (sys.version_info.major, sys.version_info.minor)
    #noreads = {'lasttime': 'None',
               #'noreadslocn': 'None',
               #'count': 'None',
               #}
    #reads = {'lasttime': 'None',
               #'readslocn': 'None',
               #'count': 'None',
               #}
    noreads = {}
    reads = {}
    AK = {}
    
    count = 0
    with open(inputfile, 'r') as FileObj:
        for line in FileObj:
            
            #if "AK>" in line:
                #akpos = line.find("AK>",0)
                #print line, akpos, line[akpos:5]  
            if "ID" in line:
                if "S?" in line:
                    noreadlocpos = line.find("ID", 0)
                    noreadslocn = line[noreadlocpos+2:noreadlocpos+7]
#                    lasttime = line[:27]
#                    noreads[lasttime] = lasttime
                    noreads[noreadslocn] = noreads.get(noreadslocn, 0) + 1
                    
                else:
                    readlocpos = line.find("ID", 0)
                    readslocn = line[readlocpos+2:readlocpos+7]
                    reads[readslocn] = reads.get(readslocn, 0) + 1
            count += 1
                    
    print
    print "Lines read: %d" % count
    print


    # Unsorted output
    #################
    
    #print "NOREADS"    
    #print "======="
    #for noreadslocn in noreads:
        #print noreadslocn, noreads[noreadslocn]
    #print
    
    #print "READS"
    #print "====="
    #for readslocn in reads:
        #print readslocn, reads[readslocn]
    #print
    

    # Sorted output
    ###############
    
    #print "Sorted Reads"
    #print "============"
    #for w in sorted(reads, key=reads.get, reverse=True):
        #print w, reads[w]
       
    #print

    #print "Sorted No-reads"
    #print "==============="
    #for w in sorted(noreads, key=noreads.get, reverse=True):
        #print w, noreads[w]
    
    #print

    
    # Sorted output with formating
    ##############################
    
    print "Loc'n"+'\t\t'+"Noreads"+'\t\t'+"Reads"+'\t\t'+"Failure Rate(%)"
    print "-----"+'\t\t'+"-------"+'\t\t'+"-----"+'\t\t'+"---------------"
    for w in sorted(noreads, key=noreads.get, reverse=True):
        percent =  (noreads[w]/reads[w]) * 100
        print str(w)+'\t\t'+str("%5d" % noreads[w])+'\t\t'+str("%5d" % reads[w])+'\t\t'+"%7.2f" % percent
    
    stop = timeit.default_timer()
    timetaken = stop - start
    print
    print "Time taken : %f seconds" % timetaken 

        

        
def rawbigcount(filename):
    f = open(filename, 'r')
    
    cur_maj_ver = sys.version_info.major
    if cur_maj_ver == 3:
        bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))    #Python 3
    elif cur_maj_ver == 2:
        bufgen = takewhile(lambda x: x, (f.read(1024*1024) for _ in repeat(None)))    #Python 2
    lines = sum( buf.count(b'\n') for buf in bufgen if buf )    
    f.close()
    return lines  


# (IMHO) the simplest approach:
def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]

# an alternative implementation, which
# happens to run a bit faster for large
# dictionaries on my machine:
def sortedDictValues2(adict):
    keys = adict.keys()
    keys.sort()
    return [dict[key] for key in keys]

def sortedDictValues3(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)


if __name__ == '__main__':
    main()
