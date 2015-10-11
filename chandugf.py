test=int(raw_input())
for i in range(test):
	length=int(raw_input())
	array=map(int, raw_input().split(" "))
	if length==len(array):
		array=reversed(sorted(array))
		print " ".join(map(str,array))
