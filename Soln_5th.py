import random
x = random.sample(range (100),10)
y = random.sample(range (20),15)
print("First List : " + str(x).strip('[]'))
print("Second List : " + str(y).strip('[]'))
a= []
for num in x:
	if num in y:
		a.append(num)
print("Common Numbers : " + str(a).strip('[]'))
