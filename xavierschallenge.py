test=input()
weight=0
li=[]
for i in range(test):
	string=raw_input()
	for letter in string:
		weight=weight+ord(letter)
	f=weight/len(string)
	if f%2==0:
		li.append(string)
	else:
		li.append(string[::-1])
for word in li:
	print word
