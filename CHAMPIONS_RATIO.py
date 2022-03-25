""" 
How it works:
First, it is checked whether an even amount of matches has been played.
Second, the program tries if an even amount of matches have been won and lost by multiplying one half with the amount of points one gasins by winning and multiplying the other half with 1, for the losses (or if an odd amount of matches have been played, a pessemistic approach is made and one more loss is taken). 
Third, the sum of this first try is substracted from the actual amount of points.
Fourth, a negative outcome means that the first guess was too much and thus overestimated the amount of wins one must have had. A positive outcome means the opposite: the residuary means that there are still points that must be accounted for, one must have won more that lost. In the case the difference is 0, the guessed amount of wins and losses are equal to the points gained, so the guess is correct.
Fifth, a new guess is made by substracting one win and adding one loss in case of a negative difference and vice versa for a positive difference.
Sixth the process repeats until the difference is zero and thus the correct amount of wins and losses are found. A message is printed with the result.   
"""

def ratio():
    print("\n\nYou choose the option to tell your win-loss ration based of the amount off games you played and points you earned.\nFirst I want to know how many games you have played")
    played = int(input())
    print("Second, how many points have you gained untill now?")
    points = int(input())
    win = 4
    loss = 1
    
    wins = (points - played)/3
    losses = played - wins
    points_wins = wins * 4
    points_losses = losses * 1
    message = "I found you ratio! You have had {} wins (accounts for {} points) and {} losses (accounts for {} points).".format(int(wins), int(points_wins), int(losses), int(points_losses))
    return message

def goal():
    print('\n\nYou choose the option to tell you how many more wins and losses you need to achieve a certain rank.\nHow many games have you played?')
    played = int(input())
    rest_matches = 20 - played
    print("Second, how many points have you gained untill now?")
    points = int(input())
    win = 4
    loss = 1
    
    ranks = [4, 12, 24, 36, 45, 51, 60, 67, 72, 76]
    
    message = ''
    for x in ranks:
        achieved = True if points >= x else False
        if achieved == False:
            needed_wins = int(((x-points) - rest_matches) / 3) + (x - rest_matches % 3 > 0) 
            needed_wins = needed_wins if needed_wins >= 0 else 0
            needed_losses = rest_matches - needed_wins if needed_wins > 0 else int((x-points) / loss)
            message += "Non achievable\n" if needed_losses < 0 else "For {} points, the minimum amount of wins are {} with {} losses \n".format(x, needed_wins, needed_losses)
        if achieved == True:
            message += 'Achieved \n'
    return message

def minimum_needed():
    print("\n\nYou choose the option to tell you what the required amount of wins and losses are to achieve any rank.\n")
    matches = 20
    win = 4
    loss = 1   
    ranks = [4, 12, 24, 36, 45, 51, 60, 67, 72, 76]
    message = ''
    
    for x in ranks:
        needed_wins = int((x - matches) / 3) + (x - matches % 3 > 0) 
        needed_wins = needed_wins if needed_wins >= 0 else 0
        needed_losses = matches - needed_wins if needed_wins > 0 else int(x / loss)
        # find minimum amount of wins and losses to achieve a rank
        message += "For {} points, the minimum amount of wins are {} with {} losses \n".format(x, needed_wins, needed_losses)
    return message

def dialogue():
    option = input()
    message = ''
    if option == '1':
        message = ratio()
    elif option == '2':
        message = goal()
    elif option == '3':
        message = minimum_needed()
    else:
        print("That is not an option you can choose. Choose again. Only the number 1, 2 and 3 are valid options.")
        message = dialogue()
    return message

print("Welcome to the FUT Champions win-loss ratio tool\nThis tool is capable of 3 different things: \n  1. Tell your win-loss ration based of the amount off games you played and points you earned;\n  2. Tell you how many more wins and losses you need to achieve a certain rank and;\n  3. Tell you what the required amount of wins and losses are to achieve any rank.\nPress 1 to 3 according to what function you want to use of this tool.")
print(dialogue())
input("Press ENTER to exit")