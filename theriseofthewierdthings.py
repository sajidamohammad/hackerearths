length=input()
zom_vam=map(int,raw_input().split(" "))
zom=[]
vam=[]
ans=[]
for i in zom_vam:
	if i%2==0:
		zom.append(i)
	else:
		vam.append(i)
zombie=sorted(zom)
vampire=sorted(vam)
for z in zombie:
	ans.append(z)
ans.append(sum(zom))
for v in vampire:
	ans.append(v)
ans.append(sum(vam))

for a in ans:
	print a,
