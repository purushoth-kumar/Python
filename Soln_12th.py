# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
a = [int(x) for x in input(). split()]
def list_ends(n):
    return[a[0], a[len(a)-1]]
print(list_ends(a))
