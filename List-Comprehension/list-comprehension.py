# liste = [10,20,30,40,50]

# sayilar = []

# for i in liste:
#     i*=2
#     sayilar.append(i)

#[(expression(ifade)) for (item) in list]#!parantez içleri değişken
# sayılar = [i for i in liste]
#!Bu şekilde kullanılır.
# isimler = ["ahmeT","vEli","ZübeYir"]
# sonuc = [isim.lower() for isim in isimler]
# print(sonuc)

###!Koşullu list comprehension###

#[(expression) for (item) in list if (koşul)]#!Bu şekilde kullanılır.

# sayilar= [1,2,3,4,5,6,7,8,9]

# sonuc = [sayi for sayi in sayilar]

# print(sonuc)

####!Uygulama####
isimler = ["Ahmet","ali","Çınar","DeNiz"]
string = "Hello 123456 World."
yillar = [1983, 1999, 2008, 1956, 1986]
dereceler = [20,5,15,-2,0,-6]

# 1- "1-100" arasındaki sayılardan 12' e tam bölünebilen sayı listesi oluşturunuz.
# sonuc = [i for i in range(1,101) if i%3==0 if i%4==0]

# 2- isimler listesindeki her ismi küçük harfe çevirip tersten yazdınız.
# sonuc = [i.lower()[::-1] for i in isimler]

# 3- verilen "string" içindeki rakamları içeren bir liste oluşturunuz.
# sonuc = [i for i in string if i.isdigit()]

# 4- "yillar" dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturunuz.
# import datetime
# simdi = datetime.datetime.now().year
# sonuc = [simdi - yil for yil in yillar]

# 5- "dereceler" listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehlikesi yazdırınız.
sonuc = [i if i>=0 else "buzlanma tehlikesi" for i in dereceler]

print(sonuc)