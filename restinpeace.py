test= int(input())
for i in range (0,test):
    temp = int(input())
    result = temp%21
    if ('21' not in str(temp) and result != 0):
        print("The streak lives still in our heart!")
    else:
        print("The streak is broken!")

