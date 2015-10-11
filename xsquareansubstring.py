tc=input()
for i in range(tc):
	s1=raw_input()
	s2=raw_input()
	for letter in s1:
		if letter in s2:
				print "Yes"
				break
		else:
				print "No"
				break
