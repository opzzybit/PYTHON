print("ROCK- PAPER- SCISSORS")

player1 = str(input("Enter rock, paper, Or scissor:  "))
player2  = str(input("Enter rock, paper, Or Scissor:  "))

if player1 == player2:
    print("Tie")
elif player1 == "rock" and player2 == "scissor":
    print("player_1 wins")

elif player1 == "scissor" and player2 == "paper":
    print("player 1 wins")

elif player1 == "Paper" and player2 == "rock":
    print("player 1 wins")

elif player2  == "rock" and player1  == "scissor":
    print("Player 2 wins")

elif player2  == "scissor" and player1 == "paper":
    print("Player 2 wins")

elif player2 == "paper" and player1  == "rock":
    print("Player 2 wins")
