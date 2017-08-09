# Ask the user for a number and determine whether the number is prime or not.
check = int(input('Enter a number to check: '))
divisors = [a for a in range(2, check) if check % a == 0]
R = ', '.join(str(x) for x in divisors)
def prime_check(n):
    if check > 1:
        if len(divisors) == 0:
            print('The entered number ', check, ' is prime')
        else:
            print('The entered number ', check, ' is NOT prime and the divisors are :\n', R)
prime_check(check)
