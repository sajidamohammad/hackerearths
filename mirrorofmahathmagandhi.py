test=input()
for i in range(test):
	num=raw_input()
	if num[::-1]==num:
		c=0
		for i in range(len(num)):
			if num[i] in ['1','0','8']:
				c=c+1
			else:
				c=c
		if c==len(num):
			print "YES"
		else:
			print "NO"	
	else:
		print "NO"
