import random
print("")

print("RASTGELE OYUN ve RAKIP SECME PROGRAMI")
print("")
print("")
import random
kisiler=["......","......","......"] # oyuncu isimleri
oyuncular=random.sample(kisiler,2)
oyun=["....",".....","......."] # oyun isimleri
oyunS=random.choice(oyun)
print(f"Secilen oyun : {oyunS}\n\nOyuncular : {oyuncular[0],oyuncular[1]}\n\nPROGRAM SONU..")