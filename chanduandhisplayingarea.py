test=input()
ans=[]
for i in range(test):
	ans.append(input())
for i in ans:
	if i%2!=0:
		i=i-1
	area=i/4
	if i%4==0:
		print area*area
	else:
		print area*(area+1)
