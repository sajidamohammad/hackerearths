from fractions import gcd
max_no=input()
friends=input()
friends_no=map(int,raw_input().split(" "))
c=0
for no in friends_no:
	if gcd(max_no,no)>1:
		c=c+1
print c
