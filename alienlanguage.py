test=input()
for i in range(test):
	jhool=raw_input()
	jaadu=raw_input()
	count=0
	for i in jaadu:
		if i in jhool:
			count+=1
	if count!=0:
		print "YES"
	else:
		print "NO"
