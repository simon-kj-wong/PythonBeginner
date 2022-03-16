import random

moves = ['rock', 'paper', 'scissors']


def rps():
    completed_games = 0
    user_wins = 0
    computer_wins = 0

    number_games = input("How many games do you want to play: ")

    while not number_games.isnumeric():
        number_games = input("Enter a valid integer: ")
    number_games = int(number_games)

    while completed_games < number_games:
        print("********************")
        user_move = input("What would you like to play: ")

        while user_move not in moves:
            user_move = input("Enter a valid move: ")
        computer_move = random.choice(moves)
        print("Computer played " + str(computer_move) + '\n')

        if user_move == computer_move:
            print("TIE!")
            continue
        elif ((user_move == 'rock' and computer_move == 'scissors') or
              (user_move == 'scissors' and computer_move == 'paper') or
              (user_move == 'paper' and computer_move == 'rock')):
            print("YOU WIN!")
            user_wins += 1
        else:
            print("YOU LOST!")
            computer_wins += 1

        if number_games > 1:
            print("Score (user, computer): " + str(user_wins) + '-' +
                  str(computer_wins))

        completed_games = user_wins + computer_wins

    print("--------------------")
    if user_wins > computer_wins:
        print("YOU WON THE MATCH!\n")
    elif user_wins < computer_wins:
        print("YOU LOST THE MATCH!\n")
    else:
        print("YOU TIED THE MATCH!\n")


if __name__ == '__main__':
    rps()
