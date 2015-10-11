import math
sm=0
test=input()
a=[]
b=[]
if (test>1 and test<100000):
	for i in range(test):
		a.append(raw_input().split(" "))
	for i in a:
		if (int(i[0])==(len(i)-1)):
			sm=sm+(len(i)-1)
			b.append(len(i)-1)
else :
	pass

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

if __name__ == '__main__':
    print nCr(sm,min(b))