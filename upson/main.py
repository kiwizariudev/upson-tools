from colorama import init, Fore, Style
import random
import requests
import os
from PIL import Image
import tkinter as tk

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def page_two():
    clear_screen()
    while True:
        clear_screen()
        print(Fore.RED + r"""

  _   _ ___  ___  ___  _  _    ___   _   __  __ ___ ___ 
 | | | | _ \/ __|/ _ \| \| |  / __| /_\ |  \/  | __/ __|
 | |_| |  _/\__ \ (_) | .` | | (_ |/ _ \| |\/| | _|\__ \
  \___/|_|  |___/\___/|_|\_|  \___/_/ \_\_|  |_|___|___/
                                 
""" + Style.RESET_ALL)

        print("1) Go to main page".ljust(25) + "2) Bank game".ljust(25) + "3) Guess the number".ljust(25) + "4) Rock Paper Scissors".ljust(25))
        print("5) Show image".ljust(25) + "6) open a windows ".ljust(25) + "7) Exit".ljust(25))

        choice = input(Fore.CYAN + "Enter your choice (1-7): " + Style.RESET_ALL)

        if choice == "1":
            return  # Quit second page and return to main menu

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
                        continue  # dont count this round

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
                image = Image.open("upson.jpg")  # place your image file here
                image.show()
            except FileNotFoundError:
                print(Fore.RED + "Image file not found." + Style.RESET_ALL)
            input("Press Enter to continue...")

        elif choice == "6":
            print("a windows is opened close it to continue")
            def open_text_window():
                window = tk.Tk()
                window.title("Custom Text Window")

                label = tk.Label(window, text="put your text here", 
                                 font=("Arial", 14), padx=20, pady=20)
                label.pack()
                window.mainloop()

            open_text_window()
            input("Press Enter to continue...")

        elif choice == "7":
            print(Fore.RED + "Exiting from page 2..." + Style.RESET_ALL)
            exit()

        else:
            print(Fore.RED + "Invalid choice, try again." + Style.RESET_ALL)
            input("Press Enter to continue...")

def main_menu():
    while True:
        clear_screen()
        print("\n" * 2)
        print(Fore.RED + r"""
  _   _ ____  ____   ___  _   _ 
 | | | |  _ \/ ___| / _ \| \ | |
 | | | | |_) \___ \| | | |  \| |
 | |_| |  __/ ___) | |_| | |\  |
  \___/|_|   |____/ \___/|_| \_|
                                
""" + Style.RESET_ALL)
        print("\nChoose an option:\n")

        print("1) Generate a number".ljust(25) + "2) Generate a phrase".ljust(25) + "3) Exit".ljust(25))
        print("4) Guess your age".ljust(25) + "5) Tell me a joke".ljust(25) + "6) Go to next page".ljust(25))

        choice = input(Fore.CYAN + "Enter your choice (1-6): " + Style.RESET_ALL)

        if choice == "1":
            number = random.randint(1, 100)
            print(Fore.GREEN + f"Generated number: {number}" + Style.RESET_ALL)
            input("Press Enter to continue...")

        elif choice == "2":
            phrases = [
                "Hello there!", "Keep going!", "Python is awesome!", "You can do it!", "Never give up!",
                "Stay focused!", "Believe in yourself!", "Try again!", "Just do it!", "Keep learning!",
                "Great job!", "Well done!", "You're amazing!", "Coding is fun!", "Success is near!"
            ]
            phrase = random.choice(phrases)
            print(Fore.YELLOW + f"Generated phrase: {phrase}" + Style.RESET_ALL)
            input("Press Enter to continue...")

        elif choice == "3":
            print(Fore.RED + "Exiting..." + Style.RESET_ALL)
            break

        elif choice == "4":
            name = input("Enter a name: ")
            response = requests.get(f"https://api.agify.io/?name={name}")
            data = response.json()
            age = data.get('age')
            if age:
                print(Fore.MAGENTA + f"Predicted age for {name} is {age}" + Style.RESET_ALL)
            else:
                print(Fore.RED + "Sorry, no age prediction found for that name." + Style.RESET_ALL)
            input("Press Enter to continue...")

        elif choice == "5":
            response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")
            joke = response.json().get("joke", "No joke found.")
            print(Fore.LIGHTBLUE_EX + f"Here's a joke: {joke}" + Style.RESET_ALL)
            input("Press Enter to continue...")

        elif choice == "6":
            page_two()

        else:
            print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
