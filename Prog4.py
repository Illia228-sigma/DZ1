# Програма 4: Вивід чисел від start до end
start = int(input("Введіть число з: "))
end = int(input("Введіть число по: "))

for num in range(start, end + 1):
    print(num, end=" ")
print()  # Для переходу на новий рядок