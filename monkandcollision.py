test=input()
array_res=[]
for i in range(test):
	array_len=input()
	array=map(int,raw_input().split(" "))
	arr_res=[]
	if array_len==len(array):
		for i in array:
			arr_res.append(i%10)
	array_res.append(len(arr_res)-len(set(arr_res)))
for i in array_res:
	print i
