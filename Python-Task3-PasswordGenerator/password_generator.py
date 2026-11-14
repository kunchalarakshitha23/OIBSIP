import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if not characters:
        return "Error: Please select at least one character type!"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("="*50)
    print("      RANDOM PASSWORD GENERATOR")
    print("      Oasis Infobyte - Task 1")
    print("="*50)
    try:
        length = int(input("\nEnter password length (e.g., 8, 12, 16): "))
        if length < 4:
            print("Password length should be at least 4 characters!")
            return
        print("\nCustomize your password (y/n):")
        use_letters = input("Include Letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include Numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Include Symbols? (y/n): ").lower() == 'y'
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print("\n" + "-"*50)
        print(f"Generated Password: {password}")
        print("-"*50)
        print(f"Password Strength: {'Strong' if length >= 12 else 'Medium' if length >= 8 else 'Weak'}")
    except ValueError:
        print("Please enter a valid number for length!")

if __name__ == "__main__":
    main()
