def proc1():
    slovo = input()
    x = ''
    while slovo != "stop1":
            x = x + slovo + ' '
            slovo = input()
    print(x)

def proc4():
    from random import randint
    m = 0
    n = 0
    while m < 3:
        a = randint(1,10)
        b = randint(1, 10)
        itog = int(input(str(a) + "+" + str(b) + "="))
        if a + b != itog:
                print("Не верно :(")
                m+=1
        else:
                print("Верно :)")
                n+=1
    if m == 3:
        print("Game over! Правильных ответов:", n)







def proc3():
    slovo = input()
    if 'ф' or 'Ф' in slovo:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово!")
proc1(), proc4(), proc3()