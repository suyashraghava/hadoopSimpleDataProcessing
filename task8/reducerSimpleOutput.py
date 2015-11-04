#!/usr/bin/python

import sys
List = []
temp = '0'
 
for line in sys.stdin:
	data = line.strip().split()
	

	if (temp == data[0]):
		if len(data) == 3:
			studentID, course, grade = data
			List.append([course,grade])
		elif len(data) == 2:
			studentID, sname = data
	else :
		print sname,
		for i in List:
			for j in i:
				print j,

		temp = data[0]
		List = []
		if len(data) == 3:
			studentID, course, grade = data
			List.append([course,grade])
		elif len(data) == 2:
			studentID, sname = data

		print '\n'
if ( temp != '0' ):
	print sname,
	for i in List:
		for j in i:
			print j,





