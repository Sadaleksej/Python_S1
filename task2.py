a = int(input("Введите число между 0 и 99999: "))

if a > 99999 or a <= 0:
    print("Некорректное число")
elif a == 1:
    print("Число простое!")

else:
    for i in range(2, int(a / 2)):
        if (a % i == 0):
            print("Число не простое!")
            break

print("Число простое!")
