   ####!Sayı tahmin uygulaması####

import random 

sayi = random.randint(1,100)
can = int(input("Kaç hak kullanmak istiyorsunuz : "))
hak = can
sayac = 0

while hak > 0:
    hak -=1
    sayac +=1
    tahmin = int(input("Tahmin ettiğiniz sayıyı yazınız: "))
    if sayi == tahmin:
        print(f"Tebrikler {sayac} .defada bildiniz. Puanınız: {100 - (100/can) * (sayac - 1 )}")
        break
    elif sayi > tahmin:
        print("Yukarı")
    else:
        print("Aşağı")

    if hak == 0:
        print(f"Hakkınız bitti.Tutulan sayı : {sayi}")        
