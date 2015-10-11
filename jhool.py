tc=input()
array=[]
for i in range(tc):
	array.append(raw_input())

for elem in array:
		
		jhool=list(elem.lstrip('www'))
		for i in jhool:
			if i in ['a','e','i','o','u']:
					while i in jhool:
						jhool.remove(i)

		print str(len(jhool))+'/'+str(len(elem))