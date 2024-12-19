import random
import string

# Step 1: Get user preferences
def get_user_preferences():
    print("Welcome to the Password Generator!")
    length = int(input("Enter password length: "))
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
    
    return length, include_lowercase, include_uppercase, include_digits, include_symbols

# Step 2: Generate password based on preferences
def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols):
    character_pool = ""
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if not character_pool:
        return "Error: No character types selected!"
    
    import secrets
    password = ''.join(secrets.choice(character_pool) for _ in range(length))

    return password

# Step 3: Main function to bring everything together
def main():
    length, use_lowercase, use_uppercase, use_digits, use_symbols = get_user_preferences()
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()