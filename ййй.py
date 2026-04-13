import re

def check_password(password):
 
    has_length = len(password) >= 8
    has_digit = bool(re.search(r"\d", password))
    has_upper = bool(re.search(r"[A-Z]", password))

    score = has_length + has_digit + has_upper
    
    print(f"Пароль: {password}")
    print(f"Баллов: {score} из 3")
    
    if score == 3:
        print("Надежный пароль!")
    else:
        print("Слабый пароль, нужно доработать.")

user_pass = input("Введите пароль: ")
check_password(user_pass)