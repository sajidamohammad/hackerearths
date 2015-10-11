test=int(raw_input())
array=[]
out=[]
count=0
for i in range(test):
	length=int(raw_input())
	for j in range(length):
		array.append(int(raw_input())
print array

for ind in range(len(array)):
	for j in range(len(array)):
		if array[ind]<array[j]:
			count=count+1
		else:
			count=0
	out.append(count)
print out
