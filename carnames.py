test=input()
for i in range(test):
	if test>=1 or test<=100:
		car_name=raw_input()
		car_names=list(set(car_name))
		if len(car_names)>3:
			print "Not OK"
		else:
			x=car_name.count(car_names[0])
			y=car_name.count(car_names[1])
			z=car_name.count(car_names[2])
			if x==y and y==z:
				print "OK"
			else:
				print "Not OK"
