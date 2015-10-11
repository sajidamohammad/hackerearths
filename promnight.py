test=input()
ans=[]
for i in range(test):
	m,n=map(int,raw_input().split(" "))
	arr_m=map(int,raw_input().split(" "))
	arr_n=map(int,raw_input().split(" "))
	arrm=sorted(arr_m)
	arrn=sorted(arr_n)
	if len(arr_m)<=len(arr_n):
		for i in range(m):
			if arrm[i]>arrn[i]:
				ans.append("YES")
				break
			else:
				ans.append("NO")
				break
	else:
		ans.append("NO")
for i in ans:
	print i
