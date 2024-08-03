first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")
if first == second != third or first != second == third or first == third != second:
    print(2)
elif first == second == third:
    print(3)
else:
    print(0)