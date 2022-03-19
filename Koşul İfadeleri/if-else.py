username = "Haşim Kılıç"
password = "12344"

isLoggedin = (username=="Haşim Kılıç") and (password=="12345")

if (isLoggedin):
    print(f"Hoşgeldiniz! {username}")
else:
    print("Yanlış bilgi girdiniz.Lütfen tekrar deneyiniz.")    