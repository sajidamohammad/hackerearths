vertices=input()
degree=map(int,raw_input().split(" "))
if vertices>=1 and vertices<=1000:
	if sum(degree)==2*(vertices-1):
		print "Yes"
	else:
		print "No"
