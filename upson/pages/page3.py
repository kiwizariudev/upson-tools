from colorama import Fore, Style
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def page3_menu():
    while True:
        clear_screen()
        print(Fore.RED + r"""

  _   _ ____  ____   ___  _   _     _   _ _____ ___ _     ___ _______   __ 
 | | | |  _ \/ ___| / _ \| \ | |   | | | |_   _|_ _| |   |_ _|_   _\ \ / / 
 | | | | |_) \___ \| | | |  \| |   | | | | | |  | || |    | |  | |  \ V /  
 | |_| |  __/ ___) | |_| | |\  |   | |_| | | |  | || |___ | |  | |   | |   
  \___/|_|   |____/ \___/|_| \_|    \___/  |_| |___|_____|___| |_|   |_|   
                                                                         
""" + Style.RESET_ALL)

        print("1) Mini calculator".ljust(25) + "2) Todo list".ljust(25) + "6) Back".ljust(25))
        choice = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL)

        if choice == "1":
            while True:
                clear_screen()
                print(Fore.GREEN + "Welcome to the mini calculator!" + Style.RESET_ALL)
                print(Fore.RED + "Type 'exit' to return to the menu." + Style.RESET_ALL)

                expression = input("Enter a calculation (e.g. 5 + 2): ")
                if expression.lower() == "exit":
                    break
                try:
                    result = eval(expression)
                    print(Fore.GREEN + f"Result: {result}" + Style.RESET_ALL)
                except:
                    print(Fore.RED + "Invalid calculation." + Style.RESET_ALL)
                input("Press Enter to continue...")

        elif choice == "2":
            list_todo = []
            while True:
                clear_screen()
                print(Fore.YELLOW + "Todo List Menu" + Style.RESET_ALL)
                print("1) Add a task".ljust(25) + "2) View tasks".ljust(25) +
                      "3) Remove a task".ljust(25) + "4) Exit".ljust(25))
                user_input = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL)

                if user_input == "1":
                    task = input("Enter the task: ")
                    list_todo.append(task)
                    print(Fore.GREEN + f"Task '{task}' added." + Style.RESET_ALL)
                elif user_input == "2":
                    if list_todo:
                        print(Fore.BLUE + "Current tasks:" + Style.RESET_ALL)
                        for i, task in enumerate(list_todo, start=1):
                            print(f"{i}. {task}")
                    else:
                        print(Fore.YELLOW + "No tasks available." + Style.RESET_ALL)
                elif user_input == "3":
                    if list_todo:
                        try:
                            task_number = int(input("Enter the task number to remove: "))
                            if 1 <= task_number <= len(list_todo):
                                removed = list_todo.pop(task_number - 1)
                                print(Fore.GREEN + f"Task '{removed}' removed." + Style.RESET_ALL)
                            else:
                                print(Fore.RED + "Invalid task number." + Style.RESET_ALL)
                        except:
                            print(Fore.RED + "Please enter a valid number." + Style.RESET_ALL)
                    else:
                        print(Fore.YELLOW + "No tasks to remove." + Style.RESET_ALL)
                elif user_input == "4":
                    print(Fore.RED + "Exiting todo list." + Style.RESET_ALL)
                    break
                input("Press Enter to continue...")

        elif choice == "6":
            break  # Return to the previous page 

        else:
            print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
            input("Press Enter to continue...")
