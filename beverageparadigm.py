import itertools
test=input()
for i in range(test):
	bev=map(int,raw_input().split(" "))
	x=input()
	perm=set(list(itertools.permutations(bev, 3)))
	sum_list=[]
	for i in perm:
		sum_list.append(sum(list(i)))
	if x in sum_list:
		print "True"
		break
	else:
		print "False"
		break
