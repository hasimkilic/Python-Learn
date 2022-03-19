       ###!String slicing (Parçalama)###
"""
ad = "Haşim"
soyad = "Kılıç"
yas = "19"

msj = "Benim adım " + ad + " ve soyadım " + soyad + "." + "Benim yaşım " + yas +"."
karakterSayisi = len(msj)

print(msj)

print(msj[karakterSayisi - 1]) # şeklinde tanımlanmalı çünkü 0 olduğundan index hatası verir.
print(msj[0])  #B
print(msj[1])  #e
print(msj[-1]) #.
print(len(msj)) #Verilen metnin kaç karakter olduğunu verir.
print(msj[0:5]) #Verilen metinde istenilen karakterler.Burada 0 ile 5(5. karakter dahil değildir) karakterler yazılır.
print(msj[:10] )#Baştan 0'dan başlar 10. karaktere kadar yazar.(10 dahil değildir.)
print(msj[10:]) #10.Karakterden başlar en sona kadar yazar.(10 dahil).
print(msj[-10:-1]) # Metnin bitişinden başlangıcına doğru yazar.(-1 dahil değil.)
print(msj[0:40:2]) #0 dan başlar 40. karaktere kadar 2 şer 2 şer atlayarak yazar.(Adım sayısı)
print(msj[::-1])#Tüm metni tersten yazar.

"""
       ###!String formatlama###
"""
ad = "Haşim"
soyad = "Kılıç"
yas = 19

print('My name is {} {} {}'.format(ad,soyad,yas)) #Sırayla normal bir şekilde yazar.
print('My name is {0} {1} {2}'.format(ad,soyad,yas))#Normal bir şekilde yazar.
print('My name is {1} {2} {0}'.format(ad,soyad,yas)) #Numaralandırdığımız formatta yazar.
print("My name is {n} {s} {a}".format(n=ad,s=soyad,a=yas)) #Tanımlandırdığımız şekilde yazar.
print("My name is {n} {s} . I'm {a} years old. ".format(n=ad,s=soyad,a=yas))#Bu şekildede yazılabilir.
print("My name is {} {} {}".format(ad,soyad,yas))

number = 200 / 700

# Bu şekilde yazdığımızda çıkan sonuç float olacağı için noktadan sonra kaç basamak geleceğini belirttik.
print("The result is {n:1.2}".format(n=number))

#Tavsiye edilen ve daha kolay bir kullanım
#Bu şekilde pr den sonra parazantez içine f yazarak daha kolay bir kulllanım elde ederiz.
print(f"My name is {ad} {soyad} and I'm {yas} years old.")
"""

         ###!String Metodları###
""" 

msg = "Python Kursumuza Hoş Geldiniz.Ben Haşim Kılıç"

sonuc = msg.upper() #!Tüm harfleri büyük harfe çevirir.
sonuc = msg.lower() #!Tüm harfleri küçük harfe çevirir.
sonuc = msg.title() #!Kelimelerin baş harflerini büyük yazar.
sonuc = msg.capitalize()#!Sadece cümlenin baş harfini büyük yazar.

sonuc = msg.islower() #!"is" ile başlayan metodlar soru sorar. Burada hepsi küçük harfli mi diye soru sorduk.
sonuc = msg.isdigit() #!Hepsi rakam mı ? diye sorduk.
sonuc = msg.isspace() #!Boşluk karakteri var mı? diye sorduk.
sonuc = "    abc  ".strip() #!Verilen ifadede boşlukları siler.
sonuc = "    abc  ".lstrip() #!Verilen ifadede soldan boşluları siler.
sonuc = "    abc  ".rstrip() #!Verilen ifadede sağdan boşluları siler.
sonuc = msg.split() #!Her bir ifadeyi boşluklardan ayırarak diziye çevirir.
sonuc = msg.split('.') #!"." dan bunları ikiye ayırarak verir.
sonuc = "-".join(sonuc) #!Bölünen her bir elemanın arasına getirir.
sonuc = msg.index("Hoş") #!Dizideki "Hoş" kelimesinin kaçıncı indexte olduğunu verir.
sonuc = msg.startswith("P") #!İfadenin hangi harf ile başladığını sorarız.True ya da false cevabını alırız.
sonuc = msg.endswith("m") #!İfadenin hangi harf ile bittiğini sorarız. True ya da false cevabını alırız. 
sonuc = msg.swapcase() #Bu ifadedeki küçük harfleri büyüğe büyükleri küçüğe çevirir.
sonuc = msg.casefold() #İfadenin aslını değiştirmeden kopyasını oluşturarak hepsini küçük harfe dönüştür.
sonuc = msg.find("H") #İfadede aradığımız elementin başlandığı indexini(konumunu) verir.İndex ile farkı index al dizede olunca hata verir find hata vermez.
sonuc = msg.replace("Haşim","Sançar") #!İfadede değiştirmek istediğimiz karakteri önce yazarız sonra yerine gelecek olanı yazarak ifadeyi değiştiririz.
sonuc = msg.replace(" ","-").replace("ş","s").replace("ı","i").replace("ç","c").replace("ö","o")
sonuc = msg.count("u"0,10) #İfadedeki gönderdiğimiz elementi kaç kere tekrarlamış onu verir.(0,10 arasında yazarsak bu index numaraları arasında arar.)
sonuc = msg.isalpha() #!İfadedeki değerlerin hepsi alafabetik mi ? diye sorar.
sonuc = "Contents.center(50,"*")#!Verilen değeri 50 index içine ortalayarak yerleştirir kalan boşluklarada "*" ifadesini ekler.
sonuc = "Contents.ljust(50,"*")#!Verilen değeri 50 index içine soldan yerleştirir kalan boşluklarada "*" ifadesini ekler.
sonuc = "Contents.rjust(50,"*")#!Verilen değeri 50 index içine sağdan yerleştirir kalan boşluklarada "*" ifadesini ekler.

print(sonuc)
"""

