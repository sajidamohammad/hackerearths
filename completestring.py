test=input()
alph='abcdefghijklmnopqrstuvwxyz'
strings=[]
for i in range(test):
	strings.append(raw_input())
for string in strings:
	string=''.join(sorted(set(string)))
	if string==alph:
		print "YES"
	else:
		print "NO"
