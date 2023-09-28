k_a='abcdefghijklmnopqrstuvwxyz'
kuc_harf=list(k_a)
b_a=k_a.upper()
buy_alf=list(b_a)
nums=[0,1,2,3,4,5,6,7,8,9]
yasak='@#!., '
ysk_list=list(yasak)
print(f'**1- Kullanici adi en az 4 en cok 16 harf olabilir.\n**2- Sifre en az 6 en fazla 12 karakter olabilir.\n**3- Kullanici adi ve parolanizda {yasak} karakterlerini kullanamazsiniz.')
uyg=True
while uyg == True:
 username=str(input('Lutfen kullanici adinizi giriniz: ')).lower().strip()
 password=(input('Lutfen sifrenizi giriniz : '))
 for i in username:
    if i in ysk_list:
     print(f'Kullanici adinda " {yasak}" kullanamazsiniz!')       #  #
     break
    elif not len(username) >= 4:
     print('Kullanici adiniz en az 4 karakter olabilir.')                    #  #
     break     
    elif not len(username) <= 16:
     print('Kullanici adiniz en fazla 16 karakter olabilir.')                #  #
     break
 for p in password:
    if p in ysk_list:
     print(f'Sifrenizde " {yasak}" kullanamazsiniz!')
     break
    elif not len(password) >= 6:
     print('Sifreniz en az 6 karakter olmalidir.')                    #  #
     break     
    elif not len(password) <= 12:
     print('Sifreniz en fazla 12 karakter olabilir.')                #  #
     break
 
    

 
    


    # and not ysk_list and i in kuc_alf or buy_alf and i in chars and i in nums and not ysk_list: