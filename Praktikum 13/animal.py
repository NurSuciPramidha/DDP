class animal:
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.berkembangbiak = berkembangbiak

    def cetak(self):
        print(f"Hewan ini bernama {self.nama}")
        print(f"Ia biasanya memakan {self.makanan}")
        print(f"Habitat atau tempat tinggalnya di {self.habitat}")
        print(f"Cara hewan ini berkembangbiak adalah dengan cara {self.berkembangbiak}")

class Musang (animal):
     def __init__(self, nama, makanan, habitat, berkembangbiak):
        super().__init__(self, nama, makanan, habitat, berkembangbiak)
        print(animal)

# cetak
a = animal("Musang", "biji-bijian", "hutan", "melahirkan")
a.cetak ()

class Kucing (animal):
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        super().__init__(self, nama, makanan, habitat, berkembangbiak)
        print(animal)

# cetak
b = animal("Kucing", "daging atau ikan", "darat", "melahirkan")
b.cetak ()

class Monyet (animal):
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        super().__init__(self, nama, makanan, habitat, berkembangbiak)
        print(animal)

# cetak
c = animal("Monyet", "buah pisang", "darat", "melahirkan")
c.cetak ()

class Badak (animal):
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        super().__init__(self, nama, makanan, habitat, berkembangbiak)
        print(animal)

# cetak
d = animal("Badak", "tumbuhan", "air", "melahirkan")
d.cetak ()

class Ular (animal):
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        super().__init__(self, nama, makanan, habitat, berkembangbiak)
        print(animal)

# cetak
e = animal("Ular", "hewan kecil", "darat", "bertelur")
e.cetak ()

class Ikan (animal):
    def __init__(self, nama, makanan, habitat, berkembangbiak):
        super().__init__(self, nama, makanan, habitat, berkembangbiak)
        print(animal)

# cetak
f = animal("Ikan", "jentik-jentik", "air", "bertelur")
f.cetak ()





        

