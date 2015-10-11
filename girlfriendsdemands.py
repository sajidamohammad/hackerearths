demand=raw_input()
l=len(demand)
q=input()
for i in range(q):
	y,n=map(int,raw_input().split(" "))
	if y<l and n<l and demand[y-1]==demand[n-1]:
		print "YES"
	elif y>l and demand[(y%l)-1]==demand[(n%l)-1]:
			print "YES"
	elif n>l and demand[(y%l)-1]==demand[(n%l)-1]:
			print "YES"
	elif y>l and n>l and demand[(y%l)-1]==demand[(n%l)-1]:
		print "YES"
	else:
		print "NO"
