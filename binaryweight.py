tc=input()
array=[]
result=[]
for i in range(tc):
		array.append(input())
for elem in array:
	for i in range(elem+1,10000):
			bine=bin(elem)
			bini=bin(i)
			if (bine.count('1')==bini.count('1')):
					result.append(i)
					break
for i in result:
	print i