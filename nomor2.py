# Meminta pengguna memasukan bilangan pertama
a = float(input("Masukkan bilangan pertama: "))

# Meminta pengguna memasukan bilangan kedua
b = float(input("Masukkan bilangan kedua: "))

# Meminta pengguna memasukan bilangan ketiga
c = float(input("Masukkan bilangan ketiga: "))

# Mengecek apakah bilangan pertama (a) lebih besar atau sama dengan bilangan kedua (b) dan bilangan ketiga (c)
# Jika benar, cetak bahwa bilangan terbesar adalah bilangan pertama (a)
if a >= b and a >= c:
    print("Bilangan terbesar adalah:", a)

# Jika kondisi pertama salah, mengecek apakah bilangan kedua (b)
elif b >= a and b >= c:
    print("Bilangan terbesar adalah:", b)

# Jika kedua kondisi sebelumnya salah, maka bilangan ketiga (c) adalah yang terbesar
else:
    print("Bilangan terbesar adalah:", c)
