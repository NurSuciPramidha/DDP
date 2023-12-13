class kucing:
    # atribut class
    nama = ""
    warna = ""
    umur = 0

    # construktor
    def __init__(self, nama, warna, umur):
        self.nama = nama
        self.warna = warna
        self.umur = umur

    # method untuk menampilkan datanya
    def data_kucing(self):
        print(f'nama kucing:{self.nama}')
        print(f'nama kucing:{self.warna}')
        print(f'nama kucing:{self.umur}')

