import random
import string

def generate_password(length):
    if length < 1:
        return "Invalid length. Please enter a positive integer."

    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt the user to enter the desired length of the password
        length = int(input("Enter the desired length of the password: "))

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
