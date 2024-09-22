import random
import string
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def generate_usernames(length, count):
    """Generates a list of random usernames"""
    characters = string.ascii_letters + string.digits  # Letters and digits
    usernames = []

    for _ in range(count):
        username = ''.join(random.choice(characters) for _ in range(length))
        usernames.append(username)

    return usernames

# Print the text in yellow
print(Fore.YELLOW + """
                      ____           _             
                     / ___| ___ _ __| | _____ _ __ 
                    | |  _ / _ \ '__| |/ / _ \ '__|
                    | |_| |  __/ |  |   <  __/ |   
                     \____|\___|_|  |_|\_\___|_|
""" + Fore.RESET)

line = r""" ============================================================================ """

print(line)

# ANSI escape code for blue
blue = '\033[34m'
reset = '\033[0m'

# Print the text in blue
print(blue + """
[---]               The 3/4 User Generator (Gerker)             [---]
[---]                Created by: AKA_Sla7er (AKA)               [---]
[---]                      Version: 1.0.0                       [---]
[---]          Homepage: https://ahmedxcx722.github.io/home/    [---]
                Welcome to the 3/4 User Generator Tool (SET)
""" + reset)

def main():
    print(Fore.RED + "Welcome To 3/4 User Generator for Hacking!" + Style.RESET_ALL) 
    while True:
        try:
            length = int(input("Enter the username length (2, 3, 4, 5): "))
            if length not in [2, 3, 4, 5]:
                print("Please enter a valid number (2, 3, 4, 5).")
                continue

            count = int(input("How many usernames would you like to generate? "))

            if count <= 0:
                print("The number of usernames should be greater than zero.")
                continue

            usernames = generate_usernames(length, count)
            print(f"Generated {count} usernames of length {length}:")
            for username in usernames:
                print(username)

        except ValueError:
            print("Error: Please enter a valid input.")
        
        cont = input("Do you want to generate more usernames? (yes/no): ").lower()
        if cont != "yes":
            print("Thank you for using the username generator!")
            break

if __name__ == "__main__":
    main()
