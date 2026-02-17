# Rock Paper Scissors Game in Python
# Author: Rafiqua Sultana
# Description: A fun command-line Rock Paper Scissors game against the computer with score tracking.

import random

def get_computer_choice():
    """Randomly pick Rock, Paper, or Scissors for the computer."""
    return random.choice(["Rock", "Paper", "Scissors"])

def get_winner(player, computer):
    """Determine the winner of a round."""
    if player == computer:
        return "tie"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Scissors" and computer == "Paper") or \
         (player == "Paper" and computer == "Rock"):
        return "player"
    else:
        return "computer"

def display_score(player_score, computer_score, ties):
    """Display the current score."""
    print("\n--- 📊 Current Score ---")
    print(f"  You     : {player_score}")
    print(f"  Computer: {computer_score}")
    print(f"  Ties    : {ties}")
    print("------------------------")

def rock_paper_scissors():
    """Main game function."""
    print("=" * 40)
    print("    🎲 Rock Paper Scissors Game!")
    print("=" * 40)
    print("  Try to beat the computer!")
    print("  First to 5 wins is the Champion! 🏆")
    print("=" * 40)

    choices = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    player_score = 0
    computer_score = 0
    ties = 0

    while player_score < 5 and computer_score < 5:
        print("\nChoose your move:")
        print("  1. 🪨  Rock")
        print("  2. 📄  Paper")
        print("  3. ✂️   Scissors")
        print("  4. 📊  View Score")
        print("  5. 🚪  Quit")
        print("-" * 40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("\nThanks for playing! Goodbye! 👋")
            break
        elif choice == "4":
            display_score(player_score, computer_score, ties)
            continue
        elif choice not in choices:
            print("❌ Invalid choice! Please enter 1, 2, 3, 4, or 5.")
            continue

        player = choices[choice]
        computer = get_computer_choice()

        print(f"\n  You chose   : {player}")
        print(f"  Computer chose: {computer}")

        result = get_winner(player, computer)

        if result == "tie":
            print("  🤝 It's a Tie!")
            ties += 1
        elif result == "player":
            print("  🎉 You Win this round!")
            player_score += 1
        else:
            print("  💻 Computer Wins this round!")
            computer_score += 1

        display_score(player_score, computer_score, ties)

    # Final result
    print("\n" + "=" * 40)
    if player_score == 5:
        print("  🏆 CONGRATULATIONS! YOU ARE THE CHAMPION!")
    elif computer_score == 5:
        print("  💻 COMPUTER WINS THE GAME! Better luck next time!")
    else:
        print("  Game Over! Thanks for playing!")

    print(f"\n  Final Score → You: {player_score} | Computer: {computer_score} | Ties: {ties}")
    print("=" * 40)

if __name__ == "__main__":
    rock_paper_scissors()
