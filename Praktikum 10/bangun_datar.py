import bangun_datar

def persegi (sisi):
    luas = sisi*sisi
    Keliling = 4*sisi
    print ("Jadi, luas persegi dengan sisi", sisi, "cm adalah", luas, "cm")
    print ("Jadi, keliling persegi dengan sisi", sisi, "cm adalah", Keliling, "cm")


def persegipanjang (panjang, lebar):
    luas = panjang*lebar
    keliling = panjang+lebar*2
    print ("Jadi, luas persegi panjang dengan panjang", panjang, "cm dan lebar", lebar, "cm adalah", luas, "cm")
    print ("jadi, keliling persegi panjang dengan panjang", panjang, "cm dan lebar", lebar, "cm adalah", keliling, "cm")


def lingkaran (jari):
    luas = 22/7*jari*jari
    keliling = 2*22/7*jari
    print ("Jadi, luas lingkaran dengan jari-jari", jari, "cm adalah", luas, "cm")
    print ("Jadi, keliling lingkaran dengan jari-jari", jari, "cm adalah", keliling, "cm")

def segitiga(sisi,alas,tinggi):
    luas = 1/2*alas*tinggi
    keliling = 3*sisi
    print("Jadi, luas segitiga dengan sisi", sisi, "cm, alas", alas, "cm dan tinggi", tinggi, "cm adalah", luas, "cm")
    print("Jadi, keliling segitiga dengan sisi", sisi, "cm, alas", alas, "cm dan tinggi", tinggi, "cm adalah", keliling, "cm")

def jajargenjang(alas,tinggi,sisi):
    luas = alas * tinggi
    keliling = 2 * (alas + sisi)
    print("Jadi luas jajargenjang yang alas dan tingginya", alas, "cm dan", tinggi, "cm adalah", luas, "cm")
    print("Jadi keliling jajargenjang yang alas dan sisinya", alas, "cm dan", sisi, "cm adalah", keliling, "cm")

def layanglayang(d1,d2,sisi1,sisi2):
    luas = 1/2 * d1 * d2
    keliling = 2 * sisi1 * sisi2
    print("Jadi luas layang-layang yang diagonal satu dan diagonal duanya", d1, "dan", d2, "adalah", luas, "cm")
    print("Jadi keliling layang-layang yang sisi-sisinya", sisi1, "dan", sisi2, "adalah", keliling, "cm")

def belahketupat(d1,d2,sisi):
    luas = 1/2 * d1 * d2
    keliling = 4 * sisi
    print("Jadi luas belahketupat yang diagonal satu dan diagonal duanya", d1, "cm dan", d2, "cm adalah", luas, "cm")
    print("Jadi keliling belahketupat yang sisi-sisinya", sisi, "cm adalah", keliling, "cm")