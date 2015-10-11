test=int(raw_input())
out=[]
arrays=[]
for i in range(test):
	arr=map(int,raw_input().split(" "))
for i in range(len(arr)):
	arrays.append(sorted(map(int,raw_input().split(" "))))
for array in arrays:
	array=sorted(array)
	out=out+array
print(" ".join(str(x) for x in reversed(sorted(out))))
