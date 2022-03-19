       ######!Break ve Continue####

#!Continue(Devam) : Oradaki kod satırı işletilmez ve diğer satıra geçer. 
#!Break(Dur,kırılma noktası) : Oraya kadarki kod satırı işletilir.Oradan sonrası yazmaz.


# name = "Haşim Kılıç"

# for a in name:
#     if (a == "K"):#!Eşit değil yaparsak Sadece bu elemanı çalıştırır.
#         continue #!'K' elemanını yazdırmadı.
#     print(a)

name = "Haşim Kılıç"

for a in name:
    if (a == "K"):
        break #!Yukarıda verdiğimiz değere kadar çalıştırır sonrasında ise durdurur.
    print(a)

