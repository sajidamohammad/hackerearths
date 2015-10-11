import sys
words = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",19:"nineteen", 20:"twenty", 21:"twenty one", 22:"twenty two", 23:"twenty three", 24:"twenty four", 25:"twenty five", 26:"twenty six", 27:"twenty seven", 28:"twenty eight", 29:"twenty nine"}
hours = input()
mins = input()
if mins == 0:
    print words[hours],"o' clock"
    sys.exit()
elif mins == 30:
    print "half past",words[hours]
    sys.exit()
if mins<30:
    if mins == 1:
        print "one minute past", words[hours]
	sys.exit()
    elif mins == 15:
        print "quarter past", words[hours]
	sys.exit()
    else:
        print words[mins],"minutes past", words[hours]
	sys.exit()
else:
    mins = 60-mins
    hours+=1
    if mins == 1:
        print "one minute to",words[hours]
	sys.exit()
    elif mins == 15:
        print "quarter to", words[hours]
	sys.exit()
    else:
        print words[mins],"minutes to",words[hours]
	sys.exit()
 
