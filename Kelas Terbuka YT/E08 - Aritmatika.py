lanjut = "Y"
while lanjut == "Y":
    a = int(input("Masukkan angka pertama = "))
    b = int(input("Masukkan angka kedua = "))
    print("="*30)
    print("Baik akan saya proses....")
    hasil = a + b
    print("Jika ditambahkan maka ",a,"+",b,"=",hasil)
    print(type(hasil))
    hasil = a - b
    print("Jika dikurangi maka ",a,"-",b,"=",hasil)
    print(type(hasil))
    hasil = a * b
    print("Jika dikalikan maka ",a,"x",b,"=",hasil)
    print(type(hasil))
    hasil = a / b
    print("Jika dibagi maka ",a,"/",b,"=",hasil)
    print(type(hasil))
    hasil = a % b
    print("Jika dibagi ",a,"%",b,"= sisa ",hasil)
    print(type(hasil))
    hasil = a // b
    print("Jika dibagi ",a,"//",b,"= terendah ",hasil)
    print(type(hasil))
    lanjut = input("Ingin ulangi lagi (Y/N)?")
