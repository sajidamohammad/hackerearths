def binary(n):
   if n > 1:
       binary(n//2)
   print(n % 2,end='')

# Take decimal number from user
dec = int(input("Enter an integer: "))
binary(dec)
