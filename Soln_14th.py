# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
a = [int(x) for x in input(). split()]


def dup_remove(x):
    return list(set(x))


print(a)
print(dup_remove(a))
