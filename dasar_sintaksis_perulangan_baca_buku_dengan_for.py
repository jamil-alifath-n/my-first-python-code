"""
Program perulangan membaca buku
"""

jumlah_buku = 10
print('Ibu memberi perintah : "Baca Buku!"')

jumlah_buku_yg_sudah_dibaca = 0
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yg_sudah_dibaca} buku")

for jumlah_buku_yg_sudah_dibaca in range (1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yg_sudah_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yg_sudah_dibaca} buku")
