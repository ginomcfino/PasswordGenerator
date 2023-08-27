import hashlib
import secrets
import string

def generate_random_password(length=16, special_chars=None):
    characters = string.ascii_letters + string.digits
    if special_chars:
        characters += special_chars
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def hash_password(password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed


if __name__=="__main__":
    print('-'*50)
    pwd_len = input('How long do you want this password? #characters=')
    special_chars = input('Any special characters you would like to use? (no space) special_characters=')
    print('-'*50)

    special_chars = ''.join(special_chars.split(' ')) #NOTE: in this case special_chars will never be None will just be ''
    try:
        password_length = int(pwd_len)
        random_password = generate_random_password(password_length, special_chars)
    except Exception as e:
        password_length = None
        print('(WARNING) Not a valid integer, using default length of 16 chars.')
        random_password = generate_random_password(special_chars=special_chars)
    
    hashed_password = hash_password(random_password)

    print()
    print("Random Password:", random_password)
    if password_length:
        print(' '*17 + '-'*password_length)
    else:
        print(' '*17 + '-'*16)
    print("Hashed Password:", hashed_password)

    print('\nPlease save your actual password somewhere secure, and used the hashed where you check your password.')

