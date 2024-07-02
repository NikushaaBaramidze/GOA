import random

def guess_number(user_number):
    if 1 <= user_number <= 1000:
        guessed_number = random.randint(1, 1000)
        if guessed_number == user_number:
            print('სწორია!')
        else
            print('არასწორია!')
        else
        print('გთხოვთ შეიყვანოთ რიცხვი 1 - დან 1000 - მდე.')


try:
    user_input = int(input("შეიყვანეთ რიცხვი 1 - დან 1000 - მდე: "))
    guess_number(user_input)
except ValueError:
    print("გთხოვთ შეიყვანოთ ვალიდური რიცხვი.")
