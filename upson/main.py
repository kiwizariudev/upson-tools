from colorama import init, Fore, Style
import random
import requests
import os

from pages.page2 import page_two  # ✅ import depuis page2.py

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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
            page_two()  # ✅ Appelle la fonction de page 2

        else:
            print(Fore.RED + "Invalid choice, please try again." + Style.RESET_ALL)
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
