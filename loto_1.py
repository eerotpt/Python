from random import randint
check = randint(0,10)

def loto():
    num = input ("Täisarv 0-9 :")
    
    if num.isdigit():
        if int(num) < check:
           print("väiksem")
           loto()
        elif int (num) > check:
           print("suurem")
           loto()
        else:
            print("niiongi")
    else:
        print("number!!!")
        loto()
loto()