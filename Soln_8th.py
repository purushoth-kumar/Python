#Make a two-player Rock-Paper-Scissors game.
import random
options = ['Rock', 'Paper', 'Scissors']
m = random.choice(options)
mc = len(m)
i = str(input("Choose one of : Rock, Paper, Scissors = "))
ic = len(i)
j = ic-mc
comp = [-1, -3, 4]
player = [-4, 1, 3]
print ("\nYou chose " + i + " and the computer chose " + m)
if j in player: print ("\nCongrats! You Win\n")
elif j in comp: print ("\nSorry! Computer Wins\n")
elif j == 0: print ("\nIt is a draw\n")
else: print ("\nYou did not choose an apropriate option.\n")

