'''import itertools
num=input()
comb=set(list(itertools.permutations(range(1,num+1),3)))
c=0
for tup in comb:
	tup=list(tup)
	if tup[0]<tup[1] and tup[1]>tup[2]:
		c=c+1
	else:
		c=c
print c'''
num=input()
if num>2:
	print (num*(num-1)*(num-2)/6)*2
