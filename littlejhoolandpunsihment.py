import math
tc=input()
if tc>=1 and tc<=50:
	for i in range(tc):
		n=input()
		b,g=map(int,raw_input().split(" "))
		if abs(b-g)>1:
			print "Little Jhool wins!"
		else:
			print "The teacher wins!"
