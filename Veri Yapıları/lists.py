 ######!Lists(Listeler)######

#!Eklemiş olduğumuz elemanların sırası önemli ise ve indexlenebilir olması,
#!gerektiği zaman kullanırız.

"""
callName = ["SamsungS5","SamsungS6","SamsungS7","SamsungS8"]

result = callName
result = len(callName)
result = callName[0]
result = callName[-1]
#callName[0] = "SamsungS9"
result = callName

# if "SamsungS6" in callName:
#     print("Evet elemanıdır.")

result = callName[-3]

del callName  [-1] #!listedeki belirtilen indexi siler.
result = callName


print(result)
"""
         ###!List Methods ###
"""         
sayilar = [1,3,5,5,7,45]
harfler = ["a","b","s","k","a"]

sonuc = min(sayilar)
sonuc = max(sayilar)

sayilar.append(10) #!Listenin en sonuna yazılan elemanı ekler.
sayilar.insert(4,5) #!Listede belirtilen sıraya ekleme yapar. 
sayilar.insert(len(sayilar),150) #!Listenin en sonuna ekler.
sayilar.pop()#!Listenin en sonundaki elemanı siler.
sayilar.pop(0)#!Listede belirtilen elemanı siler.
sayilar.remove(1,"a")#!Listede yazdığımız olan elemanı siler.
sayilar.sort() #!Listedeki elemanları alfabetik ya da büyükten küçüğe sıralar.
sayilar.reverse()#!Listedeki elemanları ters şekilde sıralar.
sayiar.count(5)#!Yazdığımız eleman listede kaç sefer tekrar ediliyor.
sayilar.index(1)#!Yazdığımız eleman listede kaçıncı indexte onu verir.
sayilar.clear()#!Listedeki bütün elemanları siler.

print(sayilar)
"""
"""
isimler = ["Ada","Veli","Haşim","Sançar"]
yaslar = [1998,2000,2002,2001]


isimler.append("Cenk")
isimler.insert(0,"Sena")
isimler.pop(1)
sonuc = isimler.index("Haşim")


print(sonuc)
"""