test=input()
marks_dict = dict()
for x in range(test):
	line = raw_input().split()
	if int(line[1]) in marks_dict:
		marks_dict[int(line[1])].append(line[0])
	else:
		marks_dict[int(line[1])] = []
		marks_dict[int(line[1])].append(line[0])
marks = sorted(marks_dict.keys(), reverse = True)
for num in marks:
	names = sorted(marks_dict[num])
	for val in names:
		print val + " " + str(num)
