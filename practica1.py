import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

default_password = generate_password()
print("Пароль из 8 символов):", default_password)
