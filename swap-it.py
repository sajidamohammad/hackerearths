test=input()
final=[]
def swapit(i,l,arr):
		for i in range(i,0,-1):
			if arr[i]<arr[i-1]:
				arr[i],arr[i-1]=arr[i-1],arr[i]
		final.append(' '.join([str(item) for item in arr]))

for j in range(test):
	l,i=map(int,raw_input().split(" "))
	arr=map(int,raw_input().split(" "))
	if i<=l:
  		swapit(i,l,arr)
for i in final:
	print i
