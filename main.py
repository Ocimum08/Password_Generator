import random
import string

def generate_password(length=12, use_special=True):
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    length = int(input("Enter password length: "))
    special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, special)
    print("Generated Password:", password)

main()
