test=raw_input()
test1=map(long,list(test))
even=[]
for i in range(len(test)):
	arr=test1[i:]
	c=0
	for i in arr:
		if i%2==0:
			c=c+1
	even.append(c)
for ev in even:
	print ev,

