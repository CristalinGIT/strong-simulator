
from random import randint

dur = 100
strength = 10
hap = 10
i = 1

def ev():
    global dur, strength, hap, i
    e = ("качать хп", "качать силу", "радоваться")
    do = ("напал враг", "светит солнце")

    while dur > 0 and hap > 0:
        print("текущий день:", i)

        print("выбери действие")
        print(*e, sep=', ')
        x = input("1/2/3: ")
        if x not in ("1", "2", "3"):
            print("неверный ввод!")
            print()
            continue
        if int(x) == 1:
            print("вы прокачали хп")
            print("+10 хп, -1 настроение")
            dur += 10
            hap -= 1

        elif int(x) == 2:
            print("вы прокачали силу")
            print("+1 сила, -1 настроение")
            strength += 1
            hap -= 1

        elif int(x) == 3:
            print("вы радуетесь")
            print("+2 настроение")
            hap += 2
        if randint(1, 5) <= 2:
            b = randint(0, len(do)-1)
            print("СОБЫТИЕ:", do[b])
            if b == 0:
                print("-30 хп")
                dur -= 30
            else:
                print("+1 настроение")
                hap += 1
        else:
            print("день прошёл спокойно")
        print("день окончен -1 настроение")
        hap -= 1

        print("текущие характеристики:")
        print("хп:", dur)
        print("сила:", strength)
        print("настроение:", hap)
        i += 1
        print()
    if dur <= 0:
        print("ты умер от потери здоровья")
    elif hap <= 0:
        print("ты впал в депрессию")
    print(f"ты прожил {i} дней")
    print(f'твоя сила = {strength}')
    if strength<20:
        print('ты хиляк')
    elif strength<50:
        print('ты качок')
    else:
        print('ты самый крутой')
ev()
