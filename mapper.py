##########################################
# Program Name: mapper.py
# Description:  Reducer program 
# Date:         10/24/2012
# Written By:   Milind Zodge
##########################################
#!/usr/bin/env python
import sys

def read_input(stdinfile):
    for line in stdinfile:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print '%s%s%d' % (word, separator, 1)

if __name__ == "__main__":
    main()
