tc=input()
num=raw_input()
numb=num.split(' ')
word_counter = {}
for word in numb:
     if word in word_counter:
         word_counter[word] += 1
     else:
         word_counter[word] = 1
for i in word_counter:
	print max(word_counter, key=word_counter.get)
	break