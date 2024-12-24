print("Welcome to Crack It!")

import random 

def get_password_list(max_passwords):
    # Get the list of passwords from the user
    print(f"Enter up to {max_passwords} passwords separated by commas (e.g., '123456, password, letmein, qwerty'): ")
    passwords = input().strip().split(",")
    if len(passwords) > max_passwords:
        print(f"Warning: You can only enter a maximum of {max_passwords} passwords. Trimming extra passwords.")
        passwords = passwords[:max_passwords]  # Trimming the list to the max password count
    return [password.strip() for password in passwords]

def choose_difficulty(): 
    # User chooses difficulty level here
    print("\nChoose difficulty level: ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    difficulty = input("Enter 1, 2, or 3: ").strip()

    if difficulty == "1":
        return {"max_attempts": 6, "passwords": 5}  # Easy: More attempts, smaller list
    elif difficulty == "2":
        return {"max_attempts": 7, "passwords": 8}  # Medium: Balanced
    elif difficulty == "3": 
        return {"max_attempts": 5, "passwords": 12}  # Hard: Fewer attempts, larger list
    else: 
        print("Invalid choice, defaulting to Medium difficulty.")
        return {"max_attempts": 7, "passwords": 8}  # Default to Medium difficulty

def give_hint(target_password, guess):
    # Provide a hint to the user based on their guess
    hint_type = random.choice(["char", "length"])  # Randomly choose hint type 
    if hint_type == "char": 
        # Provide a random character from the password
        hint_position = random.randint(0, len(target_password) - 1)
        hint = f"Hint: One character of the password is '{target_password[hint_position]}'."
    else:
        # Provide the length of the password
        hint = f"Hint: The password is {len(target_password)} characters long."
    return hint

def crack_password():
    difficulty_settings = choose_difficulty()  # Get difficulty settings
    max_passwords = difficulty_settings["passwords"]  # Get the maximum number of passwords allowed
    passwords = get_password_list(max_passwords)  # Get the list of potential passwords from user 
    print(f"Password list is: {passwords}")

    # Adjust list size based on difficulty 
    passwords = random.sample(passwords, min(len(passwords), max_passwords))  # Randomize and trim if necessary
    target_password = random.choice(passwords)  # Choose a random password from the list
    attempts = 0
    max_attempts = difficulty_settings["max_attempts"]  # Use the correct key
    print(f"\nYou have {max_attempts} attempts to guess the password!")

    while attempts < max_attempts: 
        guess = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your password guess (or type 'hint' for a hint): ").strip()

        if guess.lower() == "hint":
            hint = give_hint(target_password, guess)
            print(hint)
            continue

        attempts += 1

        if guess == target_password:
            print(f"Password cracked! The correct password is: {target_password}")
            break
        else: 
            if guess in passwords:
                print("Oops! That's not the correct password. Try again.")
            else:
                print("Oops! That password is not in the list. Try again.")

        if attempts == max_attempts:
            print(f"\nSorry, you've used all your attempts. The correct password was: {target_password}")

# Call the function to start the game
crack_password()

