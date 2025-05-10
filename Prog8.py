# Програма 8: Простий калькулятор
a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
operation = input("Введіть математичну операцію (+, -, *, /): ")

if operation == '+':
    result = a + b
    print(f"Результат: {result}")
elif operation == '-':
    result = a - b
    print(f"Результат: {result}")
elif operation == '*':
    result = a * b
    print(f"Результат: {result}")
elif operation == '/':
    if b == 0:
        print("Ділення на нуль")
    else:
        result = a / b
        print(f"Результат: {result}")
else:
    print("Невідома операція")