def eggCartons(eggs):
	six_count=0
	eight_count=0
	egg_count=eggs
	while (eggs>0):
		if eggs%8==0:
			eight_count+=1
			eggs-=8
		else:
			six_count+=1
			eggs-=6
	if (6*six_count+8*eight_count)==egg_count:
		return six_count+eight_count
	else:
		return -1


if __name__=='__main__':
	test=input()
	for i in range(test):
		eggs=input()
		print eggCartons(eggs)

