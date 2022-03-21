""" 
How it works:
First, it is checked whether an even amount of matches has been played.
Second, the program tries if an even amount of matches have been won and lost by multiplying one half with the amount of points one gasins by winning and multiplying the other half with 1, for the losses (or if an odd amount of matches have been played, a pessemistic approach is made and one more loss is taken). 
Third, the sum of this first try is substracted from the actual amount of points.
Fourth, a negative outcome means that the first guess was too much and thus overestimated the amount of wins one must have had. A positive outcome means the opposite: the residuary means that there are still points that must be accounted for, one must have won more that lost. In the case the difference is 0, the guessed amount of wins and losses are equal to the points gained, so the guess is correct.
Fifth, a new guess is made by substracting one win and adding one loss in case of a negative difference and vice versa for a positive difference.
Sixth the process repeats until the difference is zero and thus the correct amount of wins and losses are found. A message is printed with the result.   
"""

print("First I want to know how many games you have played")
played = int(input())
print("Second, how many points have you gained untill now?")
points = int(input())
win = 4
loss = 1

# to check if the amount of played matches is even
if played % 2 == 0:
    guess_win = played/2
    guess_loss = played/2
else:
    played = played - 1
    guess_win = played/2
    guess_loss = played/2+1    

middle = points - (guess_win*win + guess_loss*loss)
for x in range(1,played):
    if middle < 0:
        guess_win = guess_win-1
        guess_loss = guess_loss+1
        middle = points - (guess_win*win + guess_loss*loss)
    if middle > 0:
        guess_win = guess_win+1
        guess_loss = guess_loss-1
        middle = points - (guess_win*win + guess_loss*loss)
    if middle == 0:
        print("I found you ratio! I guessed {} wins (accounts for {} points) and {} losses (accounts for {} points).".format(int(guess_win), int(guess_win)*4, int(guess_loss), int(guess_loss)*1))
        break
        
input("Press ENTER to exit")