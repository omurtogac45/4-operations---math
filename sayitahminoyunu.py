import random
sayi=random.randint(1,20)
# print(sayi)
print("")
print("")
print("")
print("*"*25+"SAYI TAHMiN OYUNU"+"*"*25)
print("")
print("")
print("0 ile 20 arasinda tutulan sayiyi bilmeye calismalisiniz.")
print("")
print("")
print("")
can=int(input("Kac hak kullanmak istersiniz ? :  "))
hak=can
sayac=0
while hak>0:
    hak-=1
    sayac+=1
  
    tahmin=int(input(f"Tahmin {sayac}: "))

    if sayi == tahmin:
        print(f"Tutulan sayi {sayi} Tebrikler! {sayac}. denemede bildiniz! Puaniniz: {int(100-(100/can)*(sayac))}")
        break
    elif sayi>tahmin:
        print(f"Tahmininiz yanlis, tutulan sayi daha buyuk. Puaniniz :{int(100-(100/can)*(sayac))}")
    else:
        print(f"Tahmininiz yanlis, tutulan sayi daha kucuk. Puaniniz :{int(100-(100/can)*(sayac))}")
    if hak==0:
        print(f"Uzgunum hakkiniz bitti. Tutulan sayi : {sayi}")