# Програма 5: Вивід парних чисел у зворотному порядку
n = int(input("Введіть число n: "))
evens = [str(num) for num in range(n, 0, -1) if num % 2 == 0]
print(" ".join(evens))