test=input()
arr=[]
if (test<=10):
	for i in range(test):
		arr.append(input())
	for i in arr:
		print sum(range(1,i+1))
else:
	pass