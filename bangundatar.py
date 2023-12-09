#persegi
def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print("Luas Persegi: ", luas)
    print("Keliling Persegi: ", keliling)
#persegi_panjang
def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang: ", luas)
    print("Keliling Persegi Panjang: ", keliling)
#segitiga sama kaki
def segitiga_sama_sisi(alas, tinggi):
    luas = 1/2 * alas * tinggi
    keliling = 3 * alas
    print("Luas Segitiga Sama Sisi: ", luas)
    print("Keliling Segitiga Sama Sisi: ", keliling)
#jajar genjang
def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = (2 * alas) + (2 * sisi_miring)
    print("Luas Jajargenjang: ", luas)
    print("Keliling Jajargenjang: ", keliling)
#lingkaran
def lingkaran(jari_jari):
    luas = 3.14 * jari_jari * jari_jari
    keliling = 2 * 3.14 * jari_jari
    print("Luas Lingkaran: ", luas)
    print("Keliling Lingkaran: ", keliling)
#belah ketupat
def belah_ketupat(diagonal_1, diagonal_2, sisi):
    luas = 1/2 * diagonal_1 * diagonal_2
    keliling = 4 * sisi
    print("Luas Belah Ketupat: ", luas)
    print("Keliling Belah Ketupat: ", keliling)
#layang-layang
def layang_layang(diagonal_1, diagonal_2, sisi_atas, sisi_bawah):
    luas = 1/2 * diagonal_1 * diagonal_2
    keliling = (2 * sisi_atas) + (2 * sisi_bawah)
    print("Luas Layang-Layang: ", luas)
    print("Keliling Layang-Layang: ", keliling)