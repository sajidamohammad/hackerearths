test=input()
for i in range(test):
	string=raw_input().split(" ")
	for i in range(len(string)/2):
		string[i],string[len(string)-i-1]=string[len(string)-i-1],string[i]
	print ' '.join(string)
