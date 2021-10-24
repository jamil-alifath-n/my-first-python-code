daftar_buku = ['Buku 1', 'Buku 2', 'Buku 3']
print(daftar_buku)

print('\nTampil buku menggunakan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampil buku berdasarkan indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampil buku menggunakan for in range')
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal data buku')
daftar_buku = ['Buku 1', 'Buku 2', 'Buku 3', 'Buku 4']
print(daftar_buku)

print('\nMenambahkan buku dengan append')
daftar_buku.append('Buku 5')
print(daftar_buku)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama')
daftar_buku = ['Buku 1', 'Buku 2', 'Buku 3', 'Buku 4']
daftar_buku[0] = 'Buku 1 Ganti'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil buku elemen ke 2')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print('\nPop')
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -2')
daftar_buku = ['Buku 1', 'Buku 2', 'Buku 3', 'Buku 4']
daftar_buku.pop(-2)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nDel')
daftar_buku = ['Buku 1', 'Buku 2', 'Buku 3', 'Buku 4']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension')
daftar_buku = ['Buku 1', 'Buku 2', 'Buku 3', 'Buku 4']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start ')
daftar_buku = ['Buku 1', 'Buku 2', 'Buku 3', 'Buku 4']
del daftar_buku[1:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start end')
daftar_buku = ['Buku 1', 'Buku 2', 'Buku 3', 'Buku 4']
del daftar_buku[0:3]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start end')
daftar_buku = ['Buku 1', 'Buku 2', 'Buku 3', 'Buku 4']
del daftar_buku[0:-2] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del dengan list comprehension start end STEP')
daftar_buku = ['Buku 1', 'Buku 2', 'Buku 3', 'Buku 4']
del daftar_buku[0::2] #START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
