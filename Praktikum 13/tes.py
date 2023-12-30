class Manusia:
    def __init__(self, fnama, lnama):
        self.fnama = fnama
        self.lnama = lnama
    
    def cetak(self):
        print("Nama Saya", self.fnama, self.lnama)

class Staff (Manusia):
    def bekerja(self):
        print("saya pekerja keras")

class Pelajar (Manusia):
    def __init__(self, fnama, lnama, prodi, angkatan):
        super().__init__(fnama, lnama)
        self.prodi = prodi
        self.angkatan = angkatan

    def cetak (self):
        super().cetak()
        print("Saya mahasiswa angkatan", self.angkatan)

    def belajar (self):
        print("Saya adalah pelajar")

# objek manusia
x = Manusia ("Nada", "Indah")
x.cetak()

# objek staff
y = Staff ("Dedi", "rajat")
y.cetak()

# objek pelajar
z = Pelajar ("Karina", "dari prodi Sistem Informasi", "SI", "2023")
z.cetak()
