 #####!While(iken)#####

#!For döngüsü bir liste(collection) üzerinde işlem yaparken 
#!while döngüsü ise kendi koşulunu oluşturur ve onun üzerinden işlem yapar.

i = 0

# while i < 10:#!Sonsuz döngüye girer ve hata verir.Çünkü nerede duracağını bilmiyor ve aynı şeyi tekrar ediyor.
#     print("Merhaba")

# while i < 100:
#     i +=1
#     if (i%2==1):
#         print(f"tek sayı: {i}") 
#     else:
#         print(f"çift sayı:{i}")

# userName = "a"

# print(bool(userName))
#!Tanımlanmış değer içinde değişken 
#!var mı yok mu bakmak için bool değişkenini atarız varsa True yoksa False değer döner.

# userName = "a"

# while userName:#!Sonsuz döngü çünkü değer True.
#     print(f"Merhaba")

# userName = ""
# password = str("")

# while not userName:
#     userName = input("Kullanıcı adınızı giriniz:")
#     password = input("Şifrenizi giriniz:")

# print(f"Girdiğiniz kullanıcı adı: {userName}")
# print(f"Girdiğiniz şifreniz: {password}")

  ####!Uygulama####

# numbers = [4,6,9,10,35,57,89,125,244]


# for i in numbers:#!Listedeki elemanları tek tek yazar.
#     print(i)

# i = 0

# while (i<len(numbers)):#!Listedeki elemanları tek tek yazar.
#     i+=1
#     print(numbers[i])

# while numbers:#!Listedeki elemanları tek tek yazar.
#     print(numbers.pop(0))

#!Kullanıcıdan iki tane sayı alırız ve onu tek mi çift mi yazdırırız.

# baslangic = int(input("Başlangıç değerini giriniz:"))
# bitis = int(input("Bitiş değerini giriniz:"))

# i = baslangic

# while (i < bitis):
#     i+=1
#     if (i%2==1):
#         print(f"Tek sayı: {i} ")
#     else:
#         print(f"Çift sayı: {i} ") 

#!Kullanıcıdan 5 tane sayı alırız ve onu sıralayarak yazarız.

# sayilar = []
# x = 0 

# while (x<5):
#     sayi = int(input("Sayı giriniz:"))
#     sayilar.append(sayi)
#     x +=1

# sayilar.sort()
# print(sayilar)


#####!Uygulama 2#####

#    Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ürün sayısını kullanıcıya sorun.
#    dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#    ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

# i = 0
# adet = int(input('kaç adet ürün eklemek istiyorsunuz: '))
# urunler = []

# while (i < adet):
#     urunAdi = input('ürün adı: ')
#     fiyat = input('ürün fiyatı: ')
#     urunler.append({
#         'urunAdi': urunAdi,
#         'fiyat': fiyat
#     })
#     i += 1

# for urun in urunler:
#     print(f"ürün adı: {urun['urunAdi']} ürün fiyatı: {urun['fiyat']}")

# a = 0
# while (a < len(urunler)):
#     print(f"ürün adı: {urunler[a]['urunAdi']} ürün fiyatı: {urunler[a]['fiyat']}")
#     a += 1


