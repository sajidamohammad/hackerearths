test=int(raw_input())
for i in range(test):
	nkp=map(int,raw_input().split(" "))
	remove=map(int, raw_input().split(" "))
final=range(1,6)-remove
print sorted(final)[]

'''	out.append(int(raw_input()))
	for j in range(len(out)):
		if out[j] in arr:
			print "YES"
		else:
			print "NO"'''
