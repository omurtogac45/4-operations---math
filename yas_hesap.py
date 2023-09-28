import datetime
sene=datetime.datetime.now()
yil=sene.year
isDtdigit=''
while True:
 try:
  dgm=dogum=int(input('Dogum yilinizi giriniz : '))
  yas=yil-dogum
  if type(dogum)==int:
   isDtdigit=True
  if isDtdigit==True:
   print(f'Bugun itibari ile {yas} yasindasiniz.')
 except Exception as Ex:
    print('Lutfen sayi / rakam giriniz..',Ex)
 else:
  
  break


