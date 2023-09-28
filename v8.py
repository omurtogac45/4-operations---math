import random
import datetime
print('\n')
print('***'*18)
print('  v8 LUCKY BALL  '.center(54,'*'))
print('***'*18)
print('Sans Yuzdeleri ve Anlamlari'.center(51))
a,b,c=random.randint(0,101),random.randint(0,101),random.randint(0,101)
tdy=datetime.datetime.now()
gn,ay,yil=tdy.day,tdy.month,tdy.year
ort=int((a+b+c)/3)
xac,yac,zac,tac="sansini cok zorlamamalisin.",'senin gunun olabilir.','senin icin mukemmel bir gun!','gunes kesinlikle senin icin dogmus!'
print('00-40  : Sansini cok zorlamamalisin\n41-70  : Senin gunun olabilir.\n71-90  : Senin icin mukemmel bir gun!\n91-100 : Gunes bugun kesinlikle senin icin dogmus!\n')
print('***'*18)
print('\n')
hi,sbs,msj,kbgn,bbgn='Merhaba ','Senin bugunku sansin %','Sans daima sizden yana olsun. iyi gunler.','bugun','Bugun'
isim=input('Kimin sansi sorgulaniyor? : ')
secim=input('\nv8 LuckyBaLL gunluk sans oraninizi ogrenmek icin herhangi bir tusa basiniz.')
while secim !='' and isim!='':
    if 0<ort<=40:
        print(f'\n{hi}{isim}, {kbgn} {gn}.0{ay}.{yil}\n{sbs}{ort}. {bbgn} {xac}\n{msj}')
        break
    elif 40<ort<=70:
        print(f'\n{hi}{isim}, {kbgn} {gn}.0{ay}.{yil}\n{sbs}{ort}. {bbgn} {yac}\n{msj}')
        break
    elif 70<ort<=90:
        print(f'\n{hi}{isim}, {kbgn} {gn}.0{ay}.{yil}\n{sbs}{ort}. {bbgn} {zac}\n{msj}')
        break
    else:
        print(f'\n{hi}{isim}, {kbgn} {gn}.0{ay}.{yil}\n{sbs}{ort}. {bbgn} {tac}\n{msj}')
        break
else:
    secim==""
    print('Hatali giris!')
   