a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

inp = int(input("Enter a number"))

new_list = []

for i in a:
	if i < inp:
		new_list.append(i)

print (new_list)
