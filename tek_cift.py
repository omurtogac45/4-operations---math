# x=0                     # 1 den 100 e kadar olan sayilari yazdirma

# while x<=100:
#     # if x%2==1:        #  tek sayilari yazdirma
#     #  if x%2==0:        # cift sayuilari yazdirma
#       print(x)
#       x+=1          
# print("bitti..")

# ############isim girilene kadar isim grimesini isteme #########

# name= ''
# while not name.strip():
#     name=input("isminizi giriniz : ")
# print(f'Merhaba {name}.')

bsl_sayi=int(input("Baslangic sayisini giriniz : "))
son_sayi=int(input("Bitis sayisini giriniz : "))
tcn=tccevap=str(input("Tek sayilar icin 1\nCift sayilar icin 2\nButun sayilari icin 3 tuslayiniz. \n"))
x=bsl_sayi
y=son_sayi
tcn=[]
tek=1==x%2==1
cift=2==x%2==0
# print(tccevap)
while x <= y:           
 if tcn == tek:
  x+=1
  print(x%2==1) 
 elif tcn == cift:
  x+=1
  print(x%2==0)
 else:
  x+=1
  print(x)