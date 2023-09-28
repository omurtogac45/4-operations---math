def arithSum():
    return int(a)+int(b)    
def arithMin():
    return int(a)-int(b)
def arithDiv():
    return int(a)/int(b)
def arithMult():
    return int(a)*int(b)
wrngmsj='\n*** You entered not an integer.\n'.title()
longms='\n*** The entered number can be a maximum of 4 digits.\n'.title()
cntrl='\n*** Wrong or empty number selected.\n'
ZeroDivisionError='Zero Division Error'
summ='+'
minn='-'
divv='/'
multi='*'
print('\n',"Arithmetic Arranger".upper().center(57))

while True: 
 chs=input('\n* Please choose your arithmetic operation you want to perform.\n\n\t\t1-Sum\n\t\t2-Minus\n\t\t3-Divided By\n\t\t4-Multiply\n\t\t5-Quit\n\nEnter your choose: ')
 if chs.isdigit():
    if chs=='1':
     print('You choosed Sum.')  
     while True:
       
       a=input('First Number : ')
       b=input('Second Number: ')
       if len(a)<5 and len(b)<5:
        if a.isdigit() and b.isdigit():
         print(f'The result is:\n{a.rjust(6)}\n{b.rjust(6)}\n{summ}-----\n',str(arithSum()).rjust(5))
         break
        else:
         print(f'{wrngmsj}')
       else:
         print(f'{longms}')
    elif chs=='2':
      print('You choosed Minus.')
      while True:
       a=input('First Number : ')
       b=input('Second Number: ')
       if len(a)<5 and len(b)<5:
        if a.isdigit() and b.isdigit():
         print(f'The result is:\n{a.rjust(6)}\n{b.rjust(6)}\n{minn}-----\n',str(arithMin()).rjust(5))
         break
        else:
         print(f'{wrngmsj}')
       else:
        print(f'{longms}')
    elif chs=='3':
      print('You choosed Divided By.')
      while True:
       a=input('First Number : ')
       b=input('Second Number: ')
       if not a>'0' or not b>'0':
         print(f'{ZeroDivisionError}')
       elif 0<len(a)<5 and 0<len(b)<5:        
        if a.isdigit() and b.isdigit():
         print(f'The result is:\n{a.rjust(6)}\n{b.rjust(6)}\n{divv}-----\n',str(arithDiv()).rjust(5))
         break
        
        else:
         print(f'{wrngmsj}')
       else:
        print(f'{longms}')
    elif chs=='4':
        
      print('You choosed Multiply.')
      while True:
       a=input('First Number : ')
       b=input('Second Number: ')
       if len(a)<5 and len(b)<5:
        if a.isdigit() and b.isdigit():
         print(f'The result is:\n{a.rjust(6)}\n{b.rjust(6)}\n{multi}-----\n',str(arithMult()).rjust(5))
         break
        else:
         print(f'{wrngmsj}')
       else:
        print(f'{longms}')
    elif chs=='5':
      print('You choosed to Quit.\nThank you for using. Have a nice day.')  
      break
    elif chs>'5':
      print(f'{cntrl}')
 else:
   print(f'{wrngmsj}')
