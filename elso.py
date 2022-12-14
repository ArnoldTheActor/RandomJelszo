import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    length = int(input("Írja be a jelszó kívánt hosszát: "))

    alphabets_count = int(input("Írja be az ábécé karakterek mennyiségét: "))
    digits_count = int(input("Írja be a számok mennyiségét: "))
    special_characters_count = int(input("Írja be a speciális karakterek mennyiségét: "))

    characters_count = alphabets_count + digits_count + special_characters_count

    if characters_count > length:
        print("A karakterek mennyisége nagyobb, mint a jelszó hossza")
        return

    password = []

    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    for i in range(digits_count):
        password.append(random.choice(digits))

    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    random.shuffle(password)

    print("".join(password))

    print("Íme a jelszó. Ne ossza meg SENKIVEL!")


generate_random_password()
