                      ###!TUPLE###
#!Liste tipinden tek farkı elemanları değiştiremeyiz.Değiştirilmeyecek veri tuttuğumuz,
#!zaman bu liste tipini kullanırız.Liste tipine göre daha performanslıdır.      
_list = [1,2,3]
_tuple = (1,2,3,"Haşim",True,)

print(type(_list))
print(type(_tuple))
print(_tuple[4])

_list[0] = 5
#_tuple[0] = 5 #!Tuple liste tipinde eleman değişikliği yapamayız. Listeden farkı budur.


# _tuple = _tuple.index(0)#!Sadece bu iki komutu kullanabiliriz.Tuple liste tipinde.
#_tuple = _tuple.count(1)
print(_tuple)
print(_list)