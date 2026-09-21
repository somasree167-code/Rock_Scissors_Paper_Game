import random


choices = ("rock", "paper", "scissors")


def get_winner(player_choice, computer_choice):
	if player_choice == computer_choice:
		return "tie"

	winning_pairs = {
		("rock", "scissors"),
		("paper", "rock"),
		("scissors", "paper"),
	}

	return "player" if (player_choice, computer_choice) in winning_pairs else "computer"


def play_game():
	print("Rock, Paper, Scissors")
	print("Enter rock, paper, or scissors. Type quit to stop.")

	while True:
		player_choice = input("\nYour choice: ").strip().lower()

		if player_choice == "quit":
			print("Thanks for playing!")
			break

		if player_choice not in choices:
			print("Invalid choice. Please enter rock, paper, or scissors.")
			continue

		computer_choice = random.choice(choices)
		result = get_winner(player_choice, computer_choice)

		print(f"Computer chose: {computer_choice}")

		if result == "tie":
			print("It's a tie!")
		elif result == "player":
			print("You win!")
		else:
			print("Computer wins!")


if __name__ == "__main__":
	play_game()
