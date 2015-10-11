str1=raw_input()
#str2=str1.split(" ")
str3=''
for word in str1:
	for i in word:
		if i.islower() is True:
			i=i.upper()
			str3+=i
		else :
			i=i.lower()
			str3+=i
print str3
