v1=int(input("Vize 1 : "))
v2=int(input("Vize 2 : "))
fnl=int(input("Final : "))
hesap=float((((v1+v2)/2)*0.6)+(fnl*0.4))
if hesap >= 50 and fnl>50 or fnl>=70:
    print(f"Notunuz {hesap}: Gectiniz")
else:
    print(f"Notunuz {hesap}: Kaldiniz")