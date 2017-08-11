# Write a password generator in Python.
import random
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlength = int(input("How many characters do you want in your password? "))
pwd = "".join(random.sample(s, passlength))

print("The password generated is: " + pwd)
