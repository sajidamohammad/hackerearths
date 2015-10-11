import itertools
test=input()

for i in range(test):
	number=input()
	ans=[]
	if len(str(number))==1 or len(str(number))==2 :
		print "Not possible!"		
	else:
		perm=set(list(itertools.permutations(list(str(number)), len(str(number)))))
		for i in perm:
			ans.append(''.join(list(i)))
		print sorted(ans)[2],sorted(ans)[-3]
