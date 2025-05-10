# Програма 3: Гра "Вгадай число"
import random

number = random.randint(1, 10)
attempts = 3

for attempt in range(attempts):
    guess = int(input("Спробуйте вгадати число від 1 до 10: "))
    if guess == number:
        print("Вітаємо, ви вгадали число!")
        break
    elif guess > number:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Ви не вгадали число. Загадане число було: {number}")