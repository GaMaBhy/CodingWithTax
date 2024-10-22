#kita akan membuat program konversi suhu

print("Selamat Datang!\nSaya Akan membantu anda mengubah Celcius menjadi satuan suhu yang lain")

loop = "Y"
while loop == "Y":
    celcius = float(input("Masukkan Suhu dalam Celcius = "))
    fahrenheit = (celcius * 9 / 5) + 32
    kelvin = celcius + 273
    reamur = celcius * 4 / 5
    print("Baik, saya akan merubah ",celcius," celcius")
    print("="*30)
    print(celcius," Celcius = ",fahrenheit," Fahrenheit")
    print(celcius," Celcius = ",kelvin," Kelvin")
    print(celcius," Celcius = ",reamur," Reamur")
    loop = input("Ingin mengulangi lagi (Y/N)?")

