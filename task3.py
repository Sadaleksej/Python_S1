import random
randintnum = random.randint(1, 100)

for i in range (1, 10):
    a = int(input("Угадай число: "))
    if (randintnum == a):
        print("Бинго!")
        break
    elif (randintnum < a):
        print("Загаданное число меньше!")
    else:
        print("Загаданное число больше!")

print(f"Было загадано число {randintnum}")