for i in range(input()):
	string=raw_input()
	st=string.split("*")
	em=''
	for i in st:
		if 'X' not in i:
			em=em+i
	print len(em)
