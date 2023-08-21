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
    ai_score = 0
    player_score = 0
    emoji = {'rock': '🪨', 'paper': '📜', 'scissors': '✂'}
    while True:
        hands = ['rock', 'paper', 'scissors']
        ai = random.choice(hands)
        player = input("Rock, Paper or Scissors? >> ").lower()
        if player == 'exit':
            print("Thanks for playing!")
            return
        elif player not in hands:
            print("Invalid Input!")
        else:
            # validates the winner
            win = ["its a tie!", "AI Wins!", "You Win!"]
            winning_hand = game_logic(player, ai)
            if player == ai:
                winner = win[0]
            elif winning_hand == ai:
                winner = win[1]
                ai_score += 1
            else:
                winner = win[2]
                player_score += 1
            print("----")
            print("SCORE: Player", player_score, "AI", ai_score)
            print("You:", player, emoji[player])
            print("AI:", ai, emoji[ai])
            print("----")
            print(winner)


throw()

# pygames this
