# Memasukkan nilai n
n = int(input("Masukkan nilai n untuk deret Fibonacci: "))

# Inisialisasi dua bilangan pertama dalam deret Fibonacci
a, b = 0, 1
fibonacci = [a]  # Mulai dengan bilangan pertama (0)

# Menggunakan loop untuk menambahkan bilangan Fibonacci berikutnya
for i in range(1, n+1):  # Loop hingga n+1 agar mencetak n angka Fibonacci termasuk yang terakhir
    fibonacci.append(b)   
    a, b = b, a + b       

# Mencetak hasil deret Fibonacci
print(f"Deret Fibonacci hingga {n} adalah: {fibonacci}")
