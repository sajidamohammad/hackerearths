test=input()
ans=[]
for i in range(test):
	n=input()
	if n==1:
		ans.append(1)
	else:
		ans.append(n*(n+1)*2**(n - 2))
for res in ans:
	print res
