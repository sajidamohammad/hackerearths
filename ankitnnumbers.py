import itertools
test=input()
for i in  range(test):
		n=input()
		perm=set(list(itertools.permutations(range(1,n+1),)))
		print perm
