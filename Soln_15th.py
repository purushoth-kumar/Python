#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
feed = str(input("Enter the text: "))


def reverse(x):
    y = x.split()
    return " ".join(reversed(y))


print(reverse(feed))
