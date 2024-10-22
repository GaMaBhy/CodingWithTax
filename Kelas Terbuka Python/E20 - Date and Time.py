import datetime

print("Silakan masukkan tanggal lahir anda!")
tanggal = int(input("Tanggal (1-31) \t\t="))
bulan = int(input("Bulan (1-12) \t\t="))
tahun = int(input("Tahun (yyyy) \t\t="))

born = datetime.date(tahun,bulan,tanggal)

print(f"Tanggal lahir anda adalah {born}")
print(f"Hari lahir anda adalah {born:%A}")

hari_ini = datetime.date.today()
age_days = hari_ini - born
age_years = hari_ini // 365
print(f"Sedangkan hari ini adalah {hari_ini}")
print(f"Maka Usia anda adalah {age_years} tahun")
