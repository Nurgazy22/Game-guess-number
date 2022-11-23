

a = input("введите имя: ")
b = input(f"{a} хотите играть? Д/Н ")
if b == "Д":
    from random import randint
    x = randint(1,10)
    user_num = 0
    attemp = 0

    while True:
        print("Я загадал число от 1 до 10, угадайте его :) ")
        user_num = int(input("Выша догадка: "))
        attemp += 1
        if user_num == x:
            print("Молодец ты угадал число!\n Количество твоих попыток: " +str(attemp) + " Спасибо за игру!")
            print()
            more = input("Хотите еще раз сыграть? Д/Н? ")
            if more == "Д":
                continue
            else:
                break
        elif user_num < x:
            print("Мое число больше! ")
        elif user_num > x:
            print("Мое число меньше! ")
else:
    None




    
