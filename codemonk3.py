from itertools import combinations
test=input()
cost=[]
for i in range(test):
	arr=raw_input().split()

for i in range(int(arr[0])):
	cost.append(input())
a2=[c for i in range(1, len(cost)+1) for c in combinations(cost, i)]

for i in a2:
	if (sum(list(i))==int(arr[1])):
		print "YES"
		break
		
	else:
		continue		