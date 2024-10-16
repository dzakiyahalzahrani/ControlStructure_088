# Meminta pengguna untuk memasukkan nilai n
n = int(input("Masukkan nilai n: "))

# List untuk menyimpan bilangan ganjil
ganjil = []

# Loop untuk mencari bilangan ganjil hingga n
for i in range(1, n+1):
    if i % 2 != 0:  # Mengecek apakah i adalah bilangan ganjil
        ganjil.append(i)

# Mencetak hasil bilangan ganjil
print(f"Bilangan ganjil hingga {n} adalah: {ganjil}")
