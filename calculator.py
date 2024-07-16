def add(x, y):
    """Penjumlahan"""
    return x + y

def subtract(x, y):
    """Pengurangan"""
    return x - y

def multiply(x, y):
    """Perkalian"""
    return x * y

def divide(x, y):
    """Pembagian"""
    if y == 0:
        return "Error! Pembagian dengan nol tidak diperbolehkan."
    return x / y

def calculator():
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    while True:
        # Meminta input dari pengguna
        choice = input("Masukkan pilihan (1/2/3/4): ")

        # Memeriksa apakah pilihan adalah salah satu dari empat opsi
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Masukkan angka pertama: "))
                num2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
                continue

            if choice == '1':
                print(f"Hasil: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Hasil: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Hasil: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Hasil: {num1} / {num2} = {result}")

            # Tanyakan apakah pengguna ingin melakukan operasi lagi
            next_calculation = input("Ingin melakukan perhitungan lagi? (y/t): ")
            if next_calculation.lower() != 'ya':
                break
        else:
            print("Pilihan anda tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    calculator()
