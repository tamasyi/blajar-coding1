# Program Kalkulator Sederhana

print("=== Kalkulator Sederhana ===")
print("Pilih operasi:")
print("1. Tambah (+)")
print("2. Kurang (-)")
print("3. Kali (*)")
print("4. Bagi (/)")

# Meminta input pengguna
pilihan = input("Masukkan pilihan (1/2/3/4): ")

angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Logika perhitungan
if pilihan == '1':
    hasil = angka1 + angka2
    print(f"Hasil: {hasil}")
elif pilihan == '2':
    hasil = angka1 - angka2
    print(f"Hasil: {hasil}")
elif pilihan == '3':
    hasil = angka1 * angka2
    print(f"Hasil: {hasil}")
elif pilihan == '4':
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {hasil}")
    else:
        print("Error: Tidak bisa dibagi 0")
else:
    print("Pilihan tidak valid!")
