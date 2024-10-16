# Memasukkan nilai n
n = int(input("Masukkan nilai n untuk pola segitiga : "))

# Loop untuk menghasilkan pola
for i in range(1, n+1):
    # Mengubah angka i ke string dan menambahkan spasi
    # Mengulangi angka i sebanyak i kali
    print((str(i) + ' ') * i)  # Mencetak angka i sebanyak i kali
