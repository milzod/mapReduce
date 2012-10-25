##########################################
# Program Name: reducer.py
# Description:  Reducer program 
# Date:         10/24/2012
# Written By:   Milind Zodge
##########################################
#!/usr/bin/env python

from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(stdinfile, separator='\t'):
    for line in stdinfile:
        yield line.rstrip().split(separator, 1)
 
def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print "%s%s%d" % (current_word, separator, total_count)
        except ValueError:
            pass

if __name__ == "__main__":
    main()
