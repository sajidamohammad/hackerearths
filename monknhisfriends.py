test=input()
for i in range(test):
	n,m=map(int,raw_input().split(" "))
a=map(int,raw_input().split(" "))
if n+m==len(a):
	for i in range(m):
		j=n
		if a[n+i] in a[:j]:
			print "YES"
			j=j+1
		else:
			print "NO"
