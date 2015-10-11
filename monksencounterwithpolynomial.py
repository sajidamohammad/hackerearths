test=input()
for i in range(test):
	a,b,c,k=map(int,raw_input().split(" "))
	low,high=0,100000
	ans=-1
	while low<=upper:
		mid=(low+high)/2
		if (a*(mid)**2)+(b*mid)+c>=k:
			ans=mid
			high=mid-1
		else:
			low=mid+1
	print ans
