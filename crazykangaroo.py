test=input()
ans=[]
if test>=1 and test<=100000:
	for i in range(test):
		a,b,m=map(long,raw_input().split(" "))
		c=0
		if (a>=1 and b<=10**12) and (b>=1 and b<=10**12):
			ans.append(abs((b/m)-((a-1)/m)))
	for res in ans:
		print res
