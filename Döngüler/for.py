     ###!Döngüler###

#!For döngüsü bir liste(collection) üzerinde işlem yaparken 
#!while döngüsü ise kendi koşulunu oluşturur ve onun üzerinden işlem yapar.


# numbers = [1,2,3,5,6,9,15]
# names = ["Ali","Mehmet","Ayşe","Veli"]
# name = "Haşim Kılıç"
# _tuple = [(1,2),(3,4)]
# _dict = {
#     "Id":1,
#     "name":"Sançar"
# }

# for i in names:#!Numbersta kaç eleman varsa o kadar yazar.
#     print(i)

# for i in numbers:
#     print(i)

# for i in numbers:
#     print("Merhaba")

# for i in name:
#     print(i)

# for x in _dict:
#     print(_dict)#!Dict olduğu gibi yazar.

# for key,value in _dict.items():#!Hem key hemde value bilgilerini böyle yazabiliriz.
#     print(key,value)

# for x in _dict:
#     print(_dict[x])#!Dict içindeki verileri yazdırır.

# for x in _dict.values():#!Yukarıdaki döngünün aynısı bu kullanım tercih edilir.
#     print(x)    

      #####!Uygulama###

numbers = [1,2,3,4,5,15,30,35,90]

#!Tüm sayıları yazdıralım
# for i in numbers:
#     print(i)

#!5'in katı olan sayıları yazdıralım
# for number in numbers:
#     if (number % 5 == 0):
#         print(number)


#!Elemanların toplamını bulalım
# total = 0
# for number in numbers:
#     total = total + number
# print(total)

#!Çift sayıların karesi alalım.
# for number in numbers:
#     if (number % 2 == 0):
#         number = (number**2)
#         print(number)        

