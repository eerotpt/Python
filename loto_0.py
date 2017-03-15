def loto():
    num = input ("Täisarv 0-9 :")
    check = 5
    if num.isdigit():
       if int(num) < check:
        print("väiksem")
        loto()
       elif int (num) > check:
        print("suurem")
        loto()
       else: print("niiongi")
    else:
        print("number!!!")
        loto()
loto()


    