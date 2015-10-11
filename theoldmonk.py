tc=input()
while tc>=1:
	length=input()
	a=map(int,raw_input().split(" "))
	b=map(int,raw_input().split(" "))
	m=[]
	for i in xrange(length):
		for j in xrange(length):
			if b[j]>=a[i] and j>=i:
				m.append(j-i)
			else:
				m.append(0)
	print max(set(m))
	tc=tc-1a
