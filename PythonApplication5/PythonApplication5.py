
from random import randint

dur = 100
strength = 10
hap = 10
i = 1

def ev():
    global dur, strength, hap, i
    e = ("êà÷àòü õï", "êà÷àòü ñèëó", "ðàäîâàòüñÿ")
    do = ("íàïàë âðàã", "ñâåòèò ñîëíöå")

    while dur > 0 and hap > 0:
        print("òåêóùèé äåíü:", i)

        print("âûáåðè äåéñòâèå")
        print(*e, sep=', ')
        x = input("1/2/3: ")
        if x not in ("1", "2", "3"):
            print("íåâåðíûé ââîä!")
            print()
            continue
        if int(x) == 1:
            print("âû ïðîêà÷àëè õï")
            print("+10 õï, -1 íàñòðîåíèå")
            dur += 10
            hap -= 1

        elif int(x) == 2:
            print("âû ïðîêà÷àëè ñèëó")
            print("+1 ñèëà, -1 íàñòðîåíèå")
            strength += 1
            hap -= 1

        elif int(x) == 3:
            print("âû ðàäóåòåñü")
            print("+2 íàñòðîåíèå")
            hap += 2
        if randint(1, 5) <= 2:
            b = randint(0, len(do)-1)
            print("ÑÎÁÛÒÈÅ:", do[b])
            if b == 0:
                print("-30 õï")
                dur -= 30
            else:
                print("+1 íàñòðîåíèå")
                hap += 1
        else:
            print("äåíü ïðîø¸ë ñïîêîéíî")
        print("äåíü îêîí÷åí -1 íàñòðîåíèå")
        hap -= 1

        print("òåêóùèå õàðàêòåðèñòèêè:")
        print("õï:", dur)
        print("ñèëà:", strength)
        print("íàñòðîåíèå:", hap)
        i += 1
        print()
    if dur <= 0:
        print("òû óìåð îò ïîòåðè çäîðîâüÿ")
    elif hap <= 0:
        print("òû âïàë â äåïðåññèþ")
    print(f"òû ïðîæèë {i} äíåé")
    print(f'òâîÿ ñèëà = {strength}')
    if strength<20:
        print('òû õèëÿê')
    elif strength<50:
        print('òû êà÷îê')
    else:
        print('òû ñàìûé êðóòîé')
ev()
