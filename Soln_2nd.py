
check = int (input ("Enter a number: "))
pc = str (check)

if check % 4 == 0 : print ("The entered number '" + pc + "' is found to be even and also divisible by 4.")
elif check % 2 == 0 :
	print ("The entered number '" + pc + "' is found to be even.")

else:	print ("The entered number '" + pc + "' is found to be odd.")

div = int (input ("Enter second number to check divisibility: "))
pd = str (div)

if check % div == 0 : print ("The entered number '" + pc + "' is found to be divisible by '" + pd + "'.")

else: print ("The entered number '" + pc + "' is not divisible by '" + pd + "'.")
