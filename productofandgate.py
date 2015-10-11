test=int(raw_input())
an=[]
if (test >=1 and test<200):
	for j in xrange(test):
		n,k=map(int,raw_input().split(" "))
		ans=n
		for i in xrange(n,k+1):
			ans=ans&i
		an.append(ans)
for i in an:
	print i
