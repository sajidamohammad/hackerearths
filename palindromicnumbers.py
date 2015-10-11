test=input()
pn=[]
for i in range(test):
	pn.append(map(int,raw_input().split(" ")))
for li in pn:
	c=0
	if li[0]==0 and li[1]==0:
		print 1
		continue
	elif li[0]==li[1]:
		print 1
		continue
	for i in range(li[0],li[1]+1):
		if str(i)==str(i)[::-1]:
			c=c+1
	print c
