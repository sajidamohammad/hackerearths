test=int(raw_input())
arr=[]
c=0
for i in range(test):
	arr.append(int(raw_input()))
for i in arr:
	for j in range(1,i):
		if i%j==0:
			c=c+1
		else:
			c=c+0
	if c<=4:
		print "NO"
	else:
		print "YES"
