test=input()
for i in range(test):
	if test>=1 and test<=10:
		alice=list(raw_input())
		bob=list(raw_input())
		if (len(alice)>=1) and len(alice)<=10**4 and (len(bob)>=1 and len(bob)<=10**4):
			for i in alice[:]:
				if i in bob:
					alice.remove(i)
					bob.remove(i)
			if len(alice)!=0 and len(bob)!=0:
				print "You draw some."
			elif len(alice)==0 and :
				print "You lose some."
			elif len(bob)==0:
				print "You win some."
