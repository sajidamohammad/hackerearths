L=int(raw_input())
test=int(raw_input())
wl=[]
for i in range(test):
	wl.append(map(int,raw_input().split(" ")))
for li in wl:
	if li[0]<L or li[1]<L:
		print "UPLOAD ANOTHER"
	elif li[0]==li[1] and li[0]>L and li[1]>L:
		print "ACCEPTED"
	elif (li[0]>L and li[1]>L) or (li[0]>L and li[1]<=L) or (li[0]>=L and li[1]>L) :
		print "CROP IT"
	elif (li[0]==L and li[1]==L) or li[0]==li[1]:
		print "ACCEPTED"
