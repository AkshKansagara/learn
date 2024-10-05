# Password Generator Using Python 
 
import random
import string

def create_password(length):
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    chars = lower + upper + digits + special

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(chars, k=length-4)

    random.shuffle(password)

    return ''.join(password)

def main():
    length = input("Enter the desired password length: ")
    if not length.isdigit():
        print("Invalid input. Please enter a numeric value for the password length.")
        return
    length = int(length)
    if length < 4:
        print("Password length must be at least 4.")
        return
    password = create_password(length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()