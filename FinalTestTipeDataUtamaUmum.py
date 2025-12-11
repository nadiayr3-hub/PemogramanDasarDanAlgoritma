#Nomor 1
#Tipe Data  array Satu Dimensi, Dua Dimansi, dan Tiga Dimensi

print(f"---ARRAY DIMENSI 1---")
# Array 1 Dimensi
negara = ["Indonesia", "korea selatan", "swiss", "jepang"]

# Menampilkan semua elemen
print("Array 1D:")
for item in negara:
    print(item)

# Akses elemen
print("Elemen ke-2:", negara[3])

print("=" *20)

print(f'---ARRAY DIMENSI 2---')
# Array 2 Dimensi
nilai = [
    [13, 25, 90],
    [35, 68, 72],
    [80, 61, 29]
]

print("Array 2D:")
for baris in nilai:
    print(baris)

# Akses elemen baris ke-2 kolom ke-3
print("Nilai [1][2]:", nilai[1][2])

print("=" *20)

print(f"---ARRAY DIMENSI 3---")
# Array 3 Dimensi (versi variabel super unik)
galaksiData = [
    [
        [11, 22],
        [33, 44]
    ],
    [
        [55, 66],
        [77, 88]
    ]
]

print("Isi Galaksi 3D:")
for nebula in galaksiData:
    for orbit in nebula:
        print(orbit)
    print("---")

# Akses elemen lapisan 2, baris 1, kolom 2
print("Elemen terpilih:", galaksiData[1][0][1])

print("=" *20, "SELESAI", "=" *20)
