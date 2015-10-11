test = input()
array=[]
result=[]
for i in range(test):
	array.append(input())
while (len(array)>1):
	mini=min(array)
	#print mini
	array[:]=[x-mini for x in array]
	array=[elem for elem in array if elem > 0]
	array=list(set(array))
	print array
	result.append(mini*len(array))
print result
