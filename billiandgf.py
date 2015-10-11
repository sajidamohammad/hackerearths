test=input()
for i in range(test):
	a,b,k=map(int,raw_input().split(" "))
	res=a**b
	sm=0
	for i in range(k):
		sm=sm+res%10
		res=res/10
print sm
