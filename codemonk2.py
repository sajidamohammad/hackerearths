import itertools

test=input()
arr=[]
for i in range(test):
	arr.append(raw_input())
for i in arr:
	print ''.join(ch for ch, _ in itertools.groupby(i))
	