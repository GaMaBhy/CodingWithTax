#Generic Format
nama = "Agas"
format_str = f"Hello {nama}"
print(format_str)

#angka float
angka = 2005.5
format_str = f"Angka = {angka}"
print(format_str)

#angka bulat
angka = 2005
format_str = f"Angka = {angka:d}"
print(format_str)

#angka ribuan
angka = 2000
format_str = f"Ribuan = {angka:,}"
print(format_str)

#angka jutaan
angka = 2000000
format_str = f"Jutaan = {angka:,}"
print(format_str)

#angka desimal
angka = 2000000.2334
format_str = f"Jutaan = {angka:,.2f}" #2f disini berapa angka float yg mau ditampilkan
print(format_str)

#angka dengan Leading Zero
angka = 2000000.2334
format_str = f"Jutaan = {angka:015,.2f}"
print(format_str)

#angka dengan plus minus sign
plus = 17
minus = -17
cetak_plus = f"Tanda angka minus = {minus:+d}"
cetak_minus = f"Tanda angka plus = {plus:+d}"
print(cetak_plus)
print(cetak_minus)

# persentase
persen = 0.25
format_persen = f"persen = {persen:.2%}"
print(format_persen)

#format angka lain
angka = 27
binary = f"Binary = {bin(angka)}"
octal = f"Octal = {oct(angka)}"
hexa = f"Hex = {hex(angka)}"

print(binary)
print(octal)
print(hexa)