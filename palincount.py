def substring(string):
	length=len(string)
	for i in xrange(length):
		for j in range(i+1,length+1):
			yield(string[i:j])
string=raw_input()
substrings=list(substring(string))
print substrings
count=0
for sub in substrings:
	if sub==sub[::-1]:
		count+=1
print count
		
