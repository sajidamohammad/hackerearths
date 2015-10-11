tc=input()
password=[]
for i in range(tc):
	password.append(raw_input())
for elem in password:
		if (len(elem)/2!=0):
			if elem[::-1] in password :
					print str(len(elem))+" "+ elem[len(elem)/2]
					break