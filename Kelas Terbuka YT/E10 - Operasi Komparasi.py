#kita akan melakukan operasi komparasi dan membuat game tebak angka

import random
repeat = "Y"
while repeat == "Y":
    x = random.randint(1,9)

    print("==========================")
    print("|| NUMBER GUESSING GAME ||")
    print("==========================")
    print("Saya punya angka 1 sampai 9")
    print("anda tebak berapa angka saya")
    y = 0
    while y != x:
        y = int(input("Tebakan anda = "))
        print("Tebakan anda lebih besar dari Angka Saya = ",y > x)
        print("Tebakan anda kurang dari dari Angka Saya = ",y < x)
    print("===================")    
    print("Selamat anda benar!")
    print("===================")
    repeat = input("Restart Game (Y/N)? ")