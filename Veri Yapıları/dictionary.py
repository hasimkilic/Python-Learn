       ####!Dictionary(Sözlük)####

#Key-Value
#!Değişmesini istediğimiz farklı idlere sahip elemanlar yazarken kullanırız.
"""
plakalar = {
    "İstanbul":34,
    "Kayseri":38,
    "Kocaeli":41,
    "İzmir":35
}
plakalar["Rize"] = 53 #!Bu şekilde ekleme yapılıyor.

# print(f"İstanbul'un plaka kodu : {plakalar['İstanbul']} ")
# print(f"Kocaeli'nin plaka kodu : {plakalar['Kocaeli']} " )
print(plakalar)
"""
"""     ###!Uygulama 1 ####
ogrenciler = {
    100 : {
        "ad":"Haşim",
        "soyad":"Kılıç",
        "yas":19
    },
    101 : {
        "ad":"Sançar",
        "soyad":"Kılıç",
        "yas":21
    }
}
print(ogrenciler[101]["yas"])
"""
       ###!Uygulama 2 ###
"""
urunler = {}

ıd = input("Ürününüze id veriniz : ")
ad = input("Ürününüzün adını giriniz : ")
fiyat = input("Ürününüzün fiyatını giriniz: ")

urunler[ıd] = {
    "ad": ad,
    "fiyat":fiyat
}

ıd = input("Ürününüze id veriniz : ")
ad = input("Ürününüzün adını giriniz : ")
fiyat = input("Ürününüzün fiyatını giriniz: ")

urunler[ıd] = {
    "ad": ad,
    "fiyat":fiyat
}


ıd = input("Ürününüze id veriniz : ")
ad = input("Ürününüzün adını giriniz : ")
fiyat = input("Ürününüzün fiyatını giriniz: ")

urunler[ıd] = {
    "ad": ad,
    "fiyat":fiyat
}

print(urunler)
"""
         ####!Dictionary Methods####
"""
# opelObj = {
#     "marka": "Opel",
#     "model": "Corsa",
#     "Uretim Yılı":2020
# }

# sonuc = opelObj["marka"]
# sonuc = opelObj.get("marka")
# sonuc = "marka" in opelObj  #!Burada marka dict içinde mi diye soru sorduk.
# opelObj ["renk"] = "kırmızı" #!Dict e eleman eklemek istediğimizde bunu kullanırız. 
# opelObj.pop("renk") #!Yazdığımız elemanı siler. 
# opelObj.popitem()#!Son elemanı siler.
# opelObj.clear()#!dict'teki elemanları siler.


# for x in opelObj:#!Alttaki ile aynı görevi görür.
#     print(opelObj[x])

# for x in opelObj.values():#!Burada sadece elemanları yazar.
#     print(x)   

# for x,y in opelObj.items():#!Burada hem id'leri hem de elemanları yazarız.
#     print(x,y) 

# del opelObj["marka"]#!Bu şekilde del fonksiyonunu kullanarakta silme işlemi yapılır.

# obj = opelObj #!Referans kopyalama (ikiside aynı adres tutar.)
# obj = opelObj.copy() #! Kopyalama (ikiside farklı adres tutar.)

# obj ["marka"] = "Mazda"

# opelObj.update({#!Update kullanımı bu şekilde oluşuyor(Parantezlere dikkat.).Update etmek güncellemektir.
#     "marka": "Bmw",
#     "model": "520d",
#     "Uremtim Yılı": 2021
#     })



# print(obj)
# print(opelObj)
"""
          ####!Uygulama#####

players = {}

id = input("İd numarasını giriniz:")
ad = input("Oyuncu adını giriniz:")
yearsOfBirth = input("Oyuncunun doğduğu yılı giriniz:")
nationality = input("Oyuncunun ülkesini yazınız:")
current_team = input("Oyuncunun oynadığı milli takımı yazınız:")
history = input("Oyuncunun oynadığı takımları giriniz:")

players.update({
    "id":id,
    "name":ad,
    "yearsOfBirth":yearsOfBirth,
    "nationality": nationality,
    "current_team": current_team,
    "history":history
})


print(players[0])
