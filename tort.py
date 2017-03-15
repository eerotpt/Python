from math import ceil,floor


pikkus = input("Sisesta pikkus küpsistes:")
laius = input ("Laius:")
k6rgus = input ("Kõrgus:")
pakk = input ("mitu on pakis ? :")

def pakke():
    tk_arv = int( pikkus)*int(laius)*int(k6rgus)
    pakk_arv = tk_arv/int(pakk)
    print("Sul on vaja "+str(round(pakk_arv+0.49))+" pakki")
    print("Sul on vaja "+str(ceil(pakk_arv))+" pakki")
    print("Sul on vaja "+str(floor(pakk_arv))+" pakki")
pakke()


    
    