from colorama import Fore, Style
import random
import os
import requests
from PIL import Image
import tkinter as tk

from pages.page3 import page3_menu  # pour aller vers page 3

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def page_two():
    clear_screen()
    while True:
        clear_screen()
        print(Fore.RED + r"""

  _   _ ___  ___  ___  _  _      ___   _   __  __ ___ ___ 
 | | | | _ \/ __|/ _ \| \| |    / __| /_\ |  \/  | __/ __|
 | |_| |  _/\__ \ (_) | .` |   | (_ |/ _ \| |\/| | _|\__ \
  \___/|_|  |___/\___/|_|\_|    \___/_/ \_\_|  |_|___|___/
                                 
""" + Style.RESET_ALL)

        print("1) Go to main page".ljust(25) + "2) Bank game".ljust(25) + "3) Guess the number".ljust(25) + "4) Rock Paper Scissors".ljust(25))
        print("5) Show image".ljust(25) + "6) open a windows ".ljust(25) + "7) go to page 3".ljust(25) + "8) Exit".ljust(25))

        choice = input(Fore.CYAN + "Enter your choice (1-8): " + Style.RESET_ALL)

        if choice == "1":
            return  # Retour au menu principal

        elif choice == "2":
            print(Fore.GREEN + "Bank game is under construction!" + Style.RESET_ALL)
            input("Press Enter to continue...")

        elif choice == "3":
            clear_screen()
            print("Welcome to guess the number game!")
            number_to_guess = random.randint(1, 100)
            attempts = 0
            max_attempts = 10

            while attempts < max_attempts:
                try:
                    guess = int(input("Enter a number between 1 and 100: "))
                except ValueError:
                    print("Please enter a valid number!")
                    continue

                attempts += 1

                if guess < number_to_guess:
                    print("Too low.")
                elif guess > number_to_guess:
                    print("Too high.")
                else:
                    print(f"🎉 Correct! You found it in {attempts} tries.")
                    break

                print(f"Attempts left: {max_attempts - attempts}")
            else:
                print(f"❌ You lost! The number was {number_to_guess}.")

            input("Press Enter to continue...")

        elif choice == "4":
            rounds = input("How many rounds do you want to play? ")
            if not rounds.isdigit() or int(rounds) <= 0:
                print(Fore.RED + "Please enter a valid positive number for rounds." + Style.RESET_ALL)
                input("Press Enter to continue...")
            else:
                rounds = int(rounds)
                options = ["rock", "paper", "scissor"]
                beats = {
                    "paper": "rock",
                    "rock": "scissor",
                    "scissor": "paper"
                }
                player_score = 0
                bot_score = 0

                for i in range(1, rounds + 1):
                    print(f"\nRound {i} of {rounds}")
                    bot = random.choice(options)
                    player = input("Choose rock, paper, or scissor: ").strip().lower()

                    if player not in options:
                        print(Fore.RED + "Invalid choice, try again." + Style.RESET_ALL)
                        continue

                    print(f"Bot chose: {bot}")

                    if player == bot:
                        print(Fore.YELLOW + "It's a draw!" + Style.RESET_ALL)
                    elif beats[player] == bot:
                        print(Fore.GREEN + "You win this round!" + Style.RESET_ALL)
                        player_score += 1
                    else:
                        print(Fore.RED + "You lose this round!" + Style.RESET_ALL)
                        bot_score += 1

                print("\nGame Over!")
                print(f"Final Score - You: {player_score} | Bot: {bot_score}")

                if player_score > bot_score:
                    print(Fore.GREEN + "Congratulations, you won the game!" + Style.RESET_ALL)
                elif player_score < bot_score:
                    print(Fore.RED + "Sorry, you lost the game!" + Style.RESET_ALL)
                else:
                    print(Fore.YELLOW + "It's a tie game!" + Style.RESET_ALL)

                input("Press Enter to continue...")

        elif choice == "5":
            try:
                image = Image.open("upson.jpg")
                image.show()
            except FileNotFoundError:
                print(Fore.RED + "Image file not found." + Style.RESET_ALL)
            input("Press Enter to continue...")

        elif choice == "6":
            print("a windows is opened close it to continue")

            def open_text_window():
                window = tk.Tk()
                window.title("Custom Text Window")
                label = tk.Label(window, text="put your text here", font=("Arial", 14), padx=20, pady=20)
                label.pack()
                window.mainloop()

            open_text_window()
            input("Press Enter to continue...")

        elif choice == "7":
            clear_screen()
            page3_menu()
            input("press enter to continue")  # Retour menu page 2

        elif choice == "8":
            print(Fore.RED + "Exiting from page 2..." + Style.RESET_ALL)
            exit()

        else:
            print(Fore.RED + "Invalid choice, try again." + Style.RESET_ALL)
            input("Press Enter to continue...")
