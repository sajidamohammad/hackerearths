length,size=map(int,raw_input().split(" "))
array=map(int,raw_input().split(" "))
array.sort()
for i in xrange(length-1):
	if array[i+1]-array[i]>size:
		break
print array[i]
