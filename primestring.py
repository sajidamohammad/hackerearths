from math import sqrt
from itertools import count, islice
tc=input()
def isPrime(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True
	
for i in range(tc):
	string=raw_input()
	if isPrime(len(list(set(string)))):
			st_count=0
			for i in list(set(string)):
				if isPrime(string.count(i)):
					st_count+=1
				else:
					st_count=st_count
			if st_count==len(list(set(string))):
				print "YES"
			else:
				print "NO"
	else:
		print "NO"
