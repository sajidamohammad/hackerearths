test=input()
arr=[]
arr1=[]
vowel=['a','e','i','o','u','A','E','I','O','U']

if (test<=10):
	for i in range(test):
		arr.append(raw_input())
	for i in arr:
		st=""
		for j in i:
			if j in vowel :
					st=st+j
			else :
				pass
		arr1.append(st)
else:
	pass
for i in arr1:
		print i