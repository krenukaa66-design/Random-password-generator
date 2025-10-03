import string
import random

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    """
    Generate a random password.
    
    Parameters:
    - length (int): Length of the password (default 12)
    - use_upper (bool): Include uppercase letters (default True)
    - use_digits (bool): Include digits (default True)
    - use_special (bool): Include special characters (default True)
    
    Returns:
    - str: Randomly generated password
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''

    all_chars = lower + upper + digits + special

    if length < 4:
        print("⚠️ Password length should be at least 4 for security.")
        return None

    # Ensure the password has at least one character from each selected set
    password = [
        random.choice(lower),
    ]

    if use_upper:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))

    # Fill the rest of the password length with random choices from all allowed chars
    if length > len(password):
        password += random.choices(all_chars, k=length - len(password))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print("🔐 Random Password Generator")
    try:
        length = int(input("Enter password length (e.g., 12): "))
    except ValueError:
        print("Invalid input! Using default length 12.")
        length = 12

    password = generate_password(length)
    if password:
        print(f"\nGenerated Password: {password}")
