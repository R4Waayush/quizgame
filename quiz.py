#Quiz game with filehandling 
import os

# Function to handle user login
def login():
    print("=== User Login ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check credentials in the file
    if not os.path.exists("login_data.txt"):
        print("Login data file not found. Please register first.")
        return False

    with open("login_data.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if username == stored_username and password == stored_password:
                print("Login successful!")
                return True

    print("Invalid username or password.")
    return False

# Function to register a new user
def register():
    print("=== User Registration ===")
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    # Save the credentials to the file
    with open("login_data.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration successful! You can now log in.")

# Function to conduct the quiz
def quiz():
    print("=== Quiz Time ===")

    # Check if quiz file exists
    if not os.path.exists("quiz_data.txt"):
        print("Quiz data file not found...")
        return

    with open("quiz_data.txt", "r") as file:
        questions = file.readlines()

    score = 0
    for i, line in enumerate(questions):
        parts = line.strip().split(";")
        if len(parts) != 6:
            continue
        question, *options, correct_answer = parts
        print(f"\nQ{i+1}: {question}")
        for j, option in enumerate(options):
            print(f"{j+1}. {option}")

        # Get user answer
        try:
            user_answer = int(input("Your answer (1-4): "))
            if user_answer == int(correct_answer):
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {options[int(correct_answer) - 1]}")
        except ValueError:
            print("Invalid input. Skipping question.")

    print(f"\nYour total score: {score}/{len(questions)}")

# Main program
def main():
    while True:
        print("\n=== Welcome ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            if login():
                quiz()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
