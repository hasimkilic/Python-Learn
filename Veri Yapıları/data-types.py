'''
 ### !VERİ TİPLERİ ### 

# Daire alanı = πr**2
# Daire çevresi =2πr
# Yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız.
'''
'''
π = 3.14
r = int(input("Dairenin yarıçapını giriniz: "))
dAlan=(π * (r**2))
dCevre=(2 * π * r)

print("Dairenin alanı : ",dAlan)
print("Dairenin çevresi: ",dCevre)

'''
'''
# mil = km / 1.609344
# Bir aracın km cinsinden gittiği yol bilgisini mil cinsinden yazınız.

km = int(input("Kaç km yol gittiniz? "))
mil = km / 1.609344
mil = round(mil,2) # > (round) .' sonra gelen sayıların kaç tane olacağını yazdırır.

print ("Gittiğiniz ", km ," km mesafeli yolunuzun mil eşiti :",mil)

'''
