import hashlib

def crack_password(hash_to_crack, wordlist_path, hash_type='md5'):
    try:
        # Membuka file wordlist
        with open(wordlist_path, 'r') as file:
            for word in file:
                word = word.strip()  # Menghapus karakter newline
                # Buat hash dari kata dalam wordlist
                if hash_type == 'md5':
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == 'sha1':
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                elif hash_type == 'sha256':
                    hashed_word = hashlib.sha256(word.encode()).hexdigest()
                else:
                    print("Tipe hash tidak didukung!")
                    return

                # Periksa apakah hash cocok
                if hashed_word == hash_to_crack:
                    print(f"[✓] Password ditemukan: {word}")
                    return
        print("[✗] Password tidak ditemukan di wordlist.")
    except FileNotFoundError:
        print("Wordlist tidak ditemukan. Periksa path file Anda.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan
if __name__ == "__main__":
    print("Simple Password Cracker")
    hash_to_crack = input("Masukkan hash yang ingin dipecahkan: ")
    hash_type = input("Masukkan tipe hash (md5, sha1, sha256): ").lower()
    wordlist_path = input("Masukkan path ke file wordlist: ")
    crack_password(hash_to_crack, wordlist_path, hash_type)