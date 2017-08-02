num = int(input("Enter a number to know its divisors : "))

listRange = list(range(1,num+1))

divlist = []

for number in listRange:
	if num%number == 0:
		divlist.append(number)

number = str(num)
#divisor = " ".join(str(elm) for elm in divlist)
print("The divisors of " + number + " are " + str(divlist).strip('[]'))

