def main():
    import random   #brings in random module so cpu can select randomly
    score = 0  # Set score to 0

    while True: #sets the start of the loop

        choices = ["rock", "paper", "scissors"] #Set valid moves

        comp_move = random.choice(choices)  #tells cpu to pick random from choices variable
        player_move = input(str("Welcome to Rock, Paper, Scissors: Python Edition." 
        " Which one will you choose?")) .lower()             #asks for input to set player_move

        #error handling
        if player_move not in choices:
            print("That is an invalid entry. Please type 'Rock, Paper, or Scissors' and press enter.")
            continue

        print(f"AI Overlord chose: {comp_move}")  #f string allows me to call comp_move in string

        #handle ties
        if player_move == comp_move:
           print("AI Overlord made the same choice. Tie! Try again!")

        elif (player_move == "rock" and comp_move == "scissors") or \
                (player_move == "scissors" and comp_move == "paper") or \
                (player_move == "paper" and comp_move == "rock"):
            print("You win, and humanity is saved from the robots for one more day!")
            score += 1  # Increase score by 1

        else:
            print("You lose :(. Bow to your new AI king.")
            score -= 1  # Decrease score by 1

        print(f"Your current score is now {score}")

        #error handling loop again
        while True:
            play_again = input("Would you like to play again? Please Enter Yes or No:") .lower()
            if play_again == "yes":
                break


            elif play_again == "no":
                print("Thanks for playing Rock, Paper, Scissors: Python Edition")
                print("Final Score:", score)
                return   #Exit all loops and end



            else:
                print("Invalid entry. Please type 'Yes' or 'No'")
                continue














main()
