test=input()
cls=map(int,raw_input().split(" "))
clas=sorted(cls,reverse=True)
new=[]
for i in cls:
	new.append(1+clas.index(i))
for i in new:
	print i,
