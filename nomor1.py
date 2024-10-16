# Meminta pengguna memasukan nilai
nilai = input ("Masukkan nilai:")

# Mengubah input string menjadi tipe data float
nilai = float(nilai)

# Mengecek nilai apakah lebih besar atau sama dengan 90
if nilai >= 90:
    print ("Exellent performance")

# Mengecek nilai apakah lebih besar atau sama dengan 80   
elif nilai >= 80:
    print ("Very Good performance")

# Mengecek nilai apakah lebih besar atau sama dengan 70
elif nilai >= 70:
    print ("Good performance")

# Mengecek nilai apakah lebih besar atau sama dengan 60
elif nilai >= 60:
    print ("average performance")
