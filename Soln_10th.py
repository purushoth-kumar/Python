# Write a program that returns a list that contains only the elements that are
# common between the lists (without duplicates).
import random
a = random.sample(range(100), 20)
b = random.sample(range(50), 10)
c = []
for num in a:
    if num in b and num not in c:
        c.append(num)
A = ', '.join(str(x) for x in a)
B = ', '.join(str(y) for y in b)
C = ', '.join(str(z) for z in c)
print('The first random list is :' + A)
print('The second random list is : ' + B)
print('The common numbers are : ' + C)
