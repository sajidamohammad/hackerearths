from itertools import groupby
test=input()
ans=[]
def remove_dupes(arg):
    unique = (i[0] for i in groupby(arg))
    return ''.join(unique)
for i in range(test):
		string=raw_input()
		ans.append(remove_dupes(string))
for res in ans:
	print res
