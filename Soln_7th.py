#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
import random
a = []
a_length = random.randint(5,20)
while len(a) < a_length: a.append(random.randint(1,100))
even = [element for element in a if element%2==0]
str1 = ', '.join(str(e) for e in a)
str2 = ', '.join(str(i) for i in even)
print ("\nThe generated list is: " + str1)
print ("\nThe even numbers in the list are: " + str2)
