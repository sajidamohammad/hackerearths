tc=input()
if tc>=1 and tc<=10:
	for i in xrange(tc):
		string=raw_input()
		caps=0
		small=0
		if len(string)>=1 and len(string)<=100:
			for i in string :
				if i.islower():
					small+=1
				elif i.isupper():
					caps=caps+1
			if caps==0 and small==0:
				print "Invalid Input"
			elif caps==0 or small==0:
				print 0
			elif caps==small:
				print caps
			else:
				print min(caps,small)
		else: 
			print "Invalid Input"
else:
	print "Invalid Test"

