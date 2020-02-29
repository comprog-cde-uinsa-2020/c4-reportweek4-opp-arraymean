class Siswa:

    jumlah_siswa = 0

    def __init__(self, nama, nilai1, nilai2, nilai3):
        self.nama = nama
        self.nilai1 = nilai1
        self.nilai2 = nilai2
        self.nilai3 = nilai3
        Siswa.jumlah_siswa += 1

    def tampilkan_jumlah(self) :
        print( "Total siswa :",Siswa.jumlah_siswa)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("tugas pertama :", self.nilai1)
        print("tugas kedua :", self.nilai2)
        print("nilai ketiga :", self.nilai3)

    def tampilkan_rata(self) :
        rata = (self.nilai1 + self.nilai2 + self.nilai3) /3
        print ("rata-rata",self.nama, " :",rata)
        if rata < 75 :
            print ("nilai", self.nama, "dibawah kkm, harus ikut remidi")
        elif rata == 75 :
            print ("nilai", self.nama, "mencapai kkm, belajar lebih giat lagi")
        else :
            print ("nilai", self.nama, "diatas kkm, jangan mudah puas")
            
listSiswa = []
listSiswa.append(Siswa("Sarah",90,78,80))
listSiswa.append(Siswa("Budi",75,70,80))
listSiswa.append(Siswa("citra",66,56,80))

for siswa in listSiswa:
    siswa.tampilkan_profil()
    siswa.tampilkan_rata ()
