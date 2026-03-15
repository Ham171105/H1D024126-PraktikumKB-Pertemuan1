import math
import random

def main():
    print("=== program praktikum kb pertemuan 1 ===")
    
    # struktur data: list
    angka_list = [random.randint(1, 100) for _ in range(5)]
    print(f"dataset: {angka_list}")
    
    print("-" * 40)
    # struktur kontrol: perulangan
    for n in angka_list:
        # penggunaan library math
        akar = math.sqrt(n)
        
        # struktur kontrol: percabangan
        if n % 2 == 0:
            status = "genap"
        else:
            status = "ganjil"
            
        if n > 50:
            kategori = "besar"
        else:
            kategori = "kecil"
            
        print(f"angka: {n} | {status} - {kategori} | akar: {akar:.2f}")
    
    print("-" * 40)
    print("tugas selesai.")

if __name__ == "__main__":
    main()