check_point=input()
dom_chkpt=map(int,raw_input().split(" "))
brian_chkpt=map(int,raw_input().split(" "))
dom_diff=[]
brian_diff=[]
for i in range(1,check_point):
	dom_diff.append(abs(dom_chkpt[i-1]-dom_chkpt[i]))
	brian_diff.append(abs(brian_chkpt[i-1]-brian_chkpt[i]))
dom=max(dom_diff)
brian=max(brian_diff)
if dom > brian:
	print "Dom"
else:
	print "Brian"
print max(dom,brian)
