import random
import string

def create_secure_password(length=12, use_lowercase=True, use_uppercase=True, use_numbers=True, use_symbols=True):
    character_set = ''
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("At least one character type must be selected")

    # Start building the password with at least one character from each selected category
    password_chars = []
    if use_lowercase:
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_uppercase:
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password_chars.append(random.choice(string.digits))
    if use_symbols:
        password_chars.append(random.choice(string.punctuation))

    # Fill the remaining length of the password with random choices from the character set
    if length > len(password_chars):  # Ensure we don't try to choose more characters than available
        password_chars += random.choices(character_set, k=length - len(password_chars))

    random.shuffle(password_chars)

    return ''.join(password_chars)

def main():
    try:
        # Get the desired password length from the user
        desired_length = int(input("Enter the desired password length (minimum 4): "))
        if desired_length < 4:
            print("Password length should be at least 4.")
            return  

        want_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
        want_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        want_numbers = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        want_symbols = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

        generated_password = create_secure_password(
            length=desired_length,
            use_lowercase=want_lowercase,
            use_uppercase=want_uppercase,
            use_numbers=want_numbers,
            use_symbols=want_symbols
        )
        
        print("Generated Password:", generated_password)

    except ValueError as error:
        print("Error:", error)

# Run the main function
if __name__ == "__main__":

    main()
