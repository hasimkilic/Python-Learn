 #####!Sets####
#! İndexlenme önemli olmadığı zaman kullanılır.Sıralanmaz ve indexlenemez
#!Güncelleme işlemi yapamayız
#!Üzerine eleman eklemek istediğimiz zaman kullanabiliriz.

fruits = {"elma","kiraz","çilek","kavun"}
vegetables = {"bezelye","salatalık","domates"}

sonuc = fruits.add("karpuz")#!Ekleme işlemi yapar.
sonuc = "elma" in fruits#!Elemanlarda elma var mı şeklinde sorabiliriz.
fruits.update(["elma","ananas","muz"])#!Birden fazla bu şekilde eleman ekleyebiliriz.Aynı elemanı iki sefer yazmaz.
fruits.remove("karpuz")#!Silme işlemi yapılır.
# fruits.clear()#!Tüm elemanları siler.
sonuc = len(fruits)#!Elemanalrın kaç tane olduğunu verir.

sonuc = fruits
sonuc = fruits.union(vegetables)#!Farklı liste elemanları birleştirir.
print(sonuc)
