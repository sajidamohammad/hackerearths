import operator
get_bin = lambda x, n: x >= 0 and str(bin(x))[2:].zfill(n) or "-" + str(bin(x))[3:].zfill(n)
test=input()
for i in range(test):
	if test>=1 and test<=10**4:
		n,m=map(int,raw_input().split(" "))
		print map(operator.eq,str(get_bin(n,64)),str(get_bin(m,64))).count(False)
