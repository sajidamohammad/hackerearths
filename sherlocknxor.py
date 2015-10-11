import itertools
test=input()
for i in range(test):
	if test>=1 and test<=10:
		even=0
		odd=0
		length=input()
		array=map(long,raw_input().split(" "))
		for num in array:
			if num & 1==0:
				even+=1
			else:
				odd+=1
		print (even*odd)
