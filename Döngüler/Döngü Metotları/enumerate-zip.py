# enumerate
#! Bu method ifadeleri index numaralarına göre sıralamak için kullanılan bir yoldur.
#! for döngüsü içinde bu şekilde kullanılır.


markalar = ['Opel','BMW','Mercedes']

# obj1 = enumerate(markalar)


# print(list(obj1))

for a,b in enumerate(markalar):
    a +=0
    print(f"{a + 1 }-{b} ")


# zip
#!2 tane liste elemanlarını birleştirmek için kullanamya yarar.Karşılıklı eşleştirir.

liste1 = [1,2,3,4,5]
liste2 = ["a","b","c","d","e"]
liste3 = [100,200,300,400,500]

# print(list(zip(liste1,liste2)))

for k,l,m in zip(liste1,liste2,liste3):
    print(f"{k}-{l}-{m} ")
    

