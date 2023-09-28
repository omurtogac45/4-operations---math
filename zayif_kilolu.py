print("*"*50)
print("Boy - Kilo Endex Hesaplama Araci")
name=str(input("Adinizi giriniz : "))
kg=float(input("Kilonuzu giriniz : "))
hg=float(input("Boyunuzu giriniz : "))
sonuc=(kg)/(hg**2)
if  sonuc >=0 and sonuc <= 18.4 :
  print(f"Sayin {name} boy - kilo endexi hesaplama sonucun : ZAYIF")
elif sonuc > 18.4 and sonuc <=24.9:
 print(f"Sayin {name}  boy - kilo endexi hesaplama sonucun : NORMAL")
elif sonuc > 24.9 and sonuc <=29.9:
 print(f"Sayin {name}  boy - kilo endexi hesaplama sonucun : KILOLU")
else:
 print(f"Sayin {name}  boy - kilo endexi hesaplama sonucun : OBEZ")