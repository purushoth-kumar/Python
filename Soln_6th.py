#Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
word = str(input("Enter a word: "))
reverse = word[::-1]

print ("Entered word is " + word + " and its reverse is " + reverse)
if word == reverse:
	print ("Hence it is a palindrome")
else:
	print ("Hence it is NOT a palindrome")
