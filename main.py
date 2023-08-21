import random


# game logic of rock paper scissors
def game_logic(player, ai):
    if player == 'rock' and ai == 'paper' or ai == 'rock' and player == 'paper':
        return 'paper'
    elif player == 'rock' and ai == 'scissors' or ai == 'rock' and player == 'scissors':
        return 'rock'
    elif player == ai:
        return player
    else:
        return 'scissors'


# AI throws and validates player's input
def throw():
    emoji = {'rock': '🪨', 'paper': '📜', 'scissors': '✂'}
    while True:
        hands = ['rock', 'paper', 'scissors']
        ai = random.choice(hands)
        player = input("Rock, Paper or Scissors? >> ").lower()
        if player == 'exit':
            print("Thanks for playing!")
            return
        elif player not in hands:
            print("Unknown Input! Please enter Rock, Paper or Scissors.")
        else:
            print("----")
            print("You:", player, emoji[player])
            print("AI:", ai, emoji[ai])
            print("----")
            winner = game_logic(player, ai)
            if winner == player and winner == ai:
                print("Its a tie!")
            elif winner == ai:
                print("AI Wins!")
            else:
                print("You Win!")


throw()

# pygames this and add score count
