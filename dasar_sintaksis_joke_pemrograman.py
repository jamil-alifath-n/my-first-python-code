"""
Ini adalah Project demo pertama dengan Python
"""

# Sekuensial
print('Ibu menyuruh Budi pergi ke Toko!')
print('Budi menjawab: Siap pergi ke Toko!')

# Percabangan
jumlah_botol_susu = 25
jumlah_telur = 100

print(f'Jumlah botol susu: {jumlah_botol_susu} botol')
print(f'Jumlah telur: {jumlah_telur} butir')

if jumlah_botol_susu > 0:
    print('Budi mengecek harga dan ternyata uangnya cukup')
    print('Budi membeli 1 botol susu')
    if jumlah_telur > 0:
        print('Budi membeli 6 butir telur')
    else:
        print('Budi tidak membeli 6 butir telur')
else:
    print('Budi tidak jadi membeli 1 botol susu')
