import random 
import math


def isPrime(n): # n = 5
    "check if number is a prime"
    if n <= 1 : # 5 > 1
        return False
    i = 2
    while i * i <=n: # 2 * 2 = 5
        if n % i == 0: # 5 % 2 == 1
            return False # True
        i += 1 # i = 3
    return True

def generate_random_prime(min_val, max_val):
    "find a random prime number in range"
    while True:
        random_number = random.randint(min_val, max_val)
        if isPrime(random_number):
            return random_number

def create_keys():
    "create public and private keys"
    p = generate_random_prime(10, 300)
    q = generate_random_prime(10, 300)

    while p==q:
        q = generate_random_prime(10, 300)
    
    n = p * q 
    totient = (p-1) * (q-1)

    print(f"Generated primes:\np = {p}\nq = {q}\nn = {n}\nTotient = {totient}")
    while True :
        e = generate_random_prime(3, totient - 1)
        if math.gcd(e,totient) == 1 and e < totient:
            break
        else:
            continue
    # Cari Private Key (d)
    # Rumus: (d * e) % totient = 1
    # Python 3.8+ punya fungsi hebat untuk ini: pow(e, -1, totient)

    d = pow(e, -1, totient)   
    return (e, d, n)

def encrypt(plaintext, e, n):
    "encrypt plaintext using public key (e, n)"
    cipher_list = []
    for char in plaintext:
        m = ord(char)  # Convert char to ASCII
        c = pow(m, e, n)  # Encrypt using RSA formula
        cipher_list.append(c)
    return cipher_list

def decrypt(cipher_list, d, n):
    pesan_list = []
    for c in cipher_list:
        m = pow(c, d, n)  # Decrypt using RSA formula
        char = chr(m)  # Convert ASCII back to char
        pesan_list.append(char)
    return ''.join(pesan_list)

def main():
    print("--- Inisialisasi Kunci RSA ---")
    # 1. GENERATE KUNCI DI LUAR LOOP
    # Agar kunci tetap sama (konsisten) selama program berjalan
    e, d, n = create_keys()
    
    print(f"Kunci Publik (e, n) = ({e}, {n})")
    print(f"Kunci Privat (d, n) = ({d}, {n})")
    print("------------------------------")

    pesan_terakhir = []
    while True:
        print("------ RSA Key Generation ------")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. regenerate Kunci RSA (Ganti kunci baru)")
        print("4. Exit")
        choice = input("Pilih opsi (1 - 4): ")

        if choice == '1':
            print("You choose to Enkripsi.")
            # Tambahkan logika enkripsi di sini
            plaintext = input("Masukkan pesan yang akan dienkripsi: ")
            pesan_terakhir = encrypt(plaintext, e, n)
            print(f"\nPesan terenkripsi: {pesan_terakhir}")

        elif choice == '2':
            # Opsional: Bisa input manual atau pakai hasil enkripsi sebelumnya
            print(f"Mendekripsi pesan terakhir: {pesan_terakhir}")
            if not pesan_terakhir:
                print("Belum ada pesan yang dienkripsi!")
                continue
                
            # Pakai d dan n yang sudah ada
            hasil = decrypt(pesan_terakhir, d, n)
            print(f"\nHasil Dekripsi: {hasil}")

        elif choice == '3':
            # Fitur tambahan: Jika user BENAR-BENAR ingin ganti kunci
            print("Membuat pasangan kunci baru...")
            e, d, n = create_keys()
            print(f"Kunci Baru: e={e}, d={d}, n={n}")
            pesan_terakhir = [] # Reset pesan karena kunci berubah

        elif choice == '4':
            confirm = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm == 'y':
                print("Exiting the program.")
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()