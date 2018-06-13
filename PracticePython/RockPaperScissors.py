# RockPaperScissors.py
"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Rules:
-rock beats scissors
-scissors beats paper
-paper beats rock (using magic or something, common it's a rock)
"""


def get_user_y_or_n():
    while True:
        user_input = input("(Y)es or (N)o:")
        if user_input not in "YyNn":
            print("Please respond with (y)es or (n)o.")  # a little politeness goes a long way
        else:
            return user_input.lower()
        """
        user_input = str(input("(Y)es or (N)o:")).lower()
        # user_input = str(user_input).lower()
        if user_input not in ['y', 'n']:
            print("Please respond with (y)es or (n)o.")  # a little politeness goes a long way
            # print("Yes or No FOOL try AGAAAAINNNN")
        else:
            return user_input
        """


def get_user_selection():
    print("(R)ock, (P)aper, or (S)issor")
    while True:
        user_input = input("Enter Selection: ")
        if user_input not in "RrPpSs":
            print("Please enter a valid selection: (R)ock, (P)aper, or (S)issor")
        else:
            return user_input.lower()
        """
        user_input = input("Enter Selection: ")
        user_input = str(user_input).lower()
        if user_input not in ['r', 'p', 's']:
            print("Please enter a valid selection")
        else:
            return user_input
        """


def who_won(p1, p2):
    if p1 == p2:
        return 0  # tie game
    if p1 == 'r':
        if p2 == 's':
            return 1
        if p2 == 'p':
            return -1
    if p1 == 'p':
        if p2 == 's':
            return -1
        if p2 == 'r':
            return 1
    if p1 == 's':
        if p2 == 'r':
            return -1
        if p2 == 'p':
            return 1
    # if all else fails return 0
    return 0


game_running = True
# I'm uncertain, but I'm pretty sure I was highly caffinated while writing this part.
while game_running:
    print("Rock Paper Scissors!!!! MOST AWESOME GAME EVVVVAAAARRRRR\n\n")
    print("BEGIN!!!!\n\n")
    print("Player One!")
    player_1_selection = get_user_selection()
    print("Player Two!")
    player_2_selection = get_user_selection()
    winner = who_won(player_1_selection, player_2_selection)
    if winner == 0:
        print("ITS A TIE!!!!")
    elif winner == 1:
        print("PLAYER ONE DESTROYED PLAYER TWO!!!!")
    else:
        print("PLAYER TWO WRECKED PLAYER ONE!!!!")
    print("\n\n")
    print("Would you like to play ULTIMATE ROCK PAPER SCISSORS again?")
    sel = get_user_y_or_n()
    if sel == 'n':
        print("Fine... WHIMP!!!")
        quit()
    else:
        print("YEEEAAAAHHH LETS DO ITTTTT")
