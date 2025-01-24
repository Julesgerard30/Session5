# You have 3 lives. I roll the dice. If I roll a 6, you win.
# If I don't roll a 6, you lose 1 life.

from random import randint

lives = 3

while lives > 0:
    roll = randint(1, 6)  # Simulates rolling a 6-sided dice
    if roll == 6:
        print("You rolled a 6! You win!")
        break  # This exits the while loop even if lives are still > 0
    else:
        print(f"You rolled a {roll}. You lose a life.")
        lives -= 1
        print(f"Lives left: {lives}")
else:  # Executes if the while loop ends without a break
    print("You lost!")