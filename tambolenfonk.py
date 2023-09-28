girilen=int(input("Tam bolenlerini listelemek istediginiz sayiyi giriniz : "))
def tambolenbul(sayi):
    tambolenler = []
    for i in range(2,sayi):
        if (sayi % i == 0):
            tambolenler.append(i)
    return tambolenler
print(tambolenbul(girilen))