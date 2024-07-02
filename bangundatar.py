# Rumus
def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def keliling_segitiga(alas, sisi1, sisi2):
    return alas + sisi1 + sisi2 

#input untuk memilih bangun datar
def hitung_bangun_datar():
    pilihan = int(input("Pilih bangun datar:\n1. Persegi \n2. Persegi Panjang\n3. Segitiga\nMasukkan pilihan (1/2/3): "))
    
    #Input untuk memasukkan nilai untuk dihitung berdasarkan bangun datar yang dipilih
    if pilihan == 1:
        sisi = float(input("Masukkan panjang sisi Persegi: "))
        if sisi <= 0:
            print("Nilai sisi harus positif!")
            return
        luas = luas_persegi(sisi)
        keliling = keliling_persegi(sisi)
        print(f"Luas persegi dengan sisi {sisi} adalah {luas}")
        print(f"Keliling persegi dengan sisi {sisi} adalah {keliling}")
        
    elif pilihan == 2:
        panjang = float(input("Masukkan panjang Persegi Panjang: "))
        lebar = float(input("Masukkan lebar Persegi Panjang: "))
        if panjang <= 0 or lebar <= 0:
            print("Nilai panjang dan lebar harus positif!")
            return
        luas = luas_persegi_panjang(panjang, lebar)
        keliling = keliling_persegi_panjang(panjang, lebar)
        print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")
        print(f"Keliling persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {keliling}")
        
    elif pilihan == 3:
        alas = float(input("Masukkan panjang alas Segitiga: "))
        tinggi = float(input("Masukkan tinggi Segitiga: "))
        sisi1 = float(input("Masukkan sisi pertama Segitiga: "))
        sisi2 = float(input("Masukkan sisi kedua Segitiga: "))
        if alas <= 0 or tinggi <= 0 or sisi1 <= 0 or sisi2 <= 0:
            print("Nilai alas, tinggi, dan sisi harus positif!")
            return
        luas = luas_segitiga(alas, tinggi)
        keliling = keliling_segitiga(alas, sisi1, sisi2)
        print(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}")
        print(f"Keliling segitiga dengan alas {alas}, sisi pertama {sisi1}, dan sisi kedua {sisi2} adalah {keliling}")
        
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1, 2, dan 3")

while True:
    hitung_bangun_datar()
    ulangi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ").lower()
    if ulangi != 'ya':
        print("Terima kasih telah menggunakan program ini!")
        break
