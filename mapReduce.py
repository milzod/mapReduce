##########################################
# Program Name: mapReduce.py
# Description:  Map Reduce program 
# Date:         09/18/2012
# Written By:   Milind Zodge
##########################################
print('Map Reduce Program')
dlist = {}
infile=open('first.txt', 'r')
line=infile.readline()
#print('line: ' + line)
while (line):
	lst=line.split(' ')
	for word in lst:
		#print('word: ' + word)
		if not word in dlist:
		        dlist[word] = 1
		else:
		        dlist[word] += 1
	line=infile.readline()
print (dlist)