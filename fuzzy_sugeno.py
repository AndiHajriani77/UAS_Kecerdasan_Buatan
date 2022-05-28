#Fuzzy Sugeno
#Studi Kasus : Permintaan Penjualan Minyak Goreng 

#Nama   : Andi Hajriani
#Nim    : 191011401857
#Kelas  : 06TPLE025 

#Kecepatan Debit Minyak  : min 2 liter/detik dan max 4 liter/detik.
#Banyaknya Minyak  : sedikit 50L dan banyak 150L.
#Tingkat kecepatan mesin : rendah 20, sedang 30, dan 40 tinggi.


def down(x, xmin, xmax):
    return (xmax- x) / (xmax - xmin)

def up(x, xmin, xmax):
    return (x - xmin) / (xmax - xmin)

class Minyak():
    minimum = 50
    maximum = 150

    def sedikit(self, x):
        if x >= self.maximum:
            return 0
        elif x <= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.maximum)

    def banyak(self, x):
        if x <= self.minimum:
            return 0
        elif x >= self.maximum:
            return 1
        else:
            return up(x, self.minimum, self.maximum)
        class Mesin():
        minimum = 20
    medium = 30
    maximum = 40

    def rendah(self, x):
        if x >= self.medium:
            return 0
        elif x <= self.minimum:
            return 1
        else:
            return down(x, self.minimum, self.medium)
    
    def sedang(self, x):
        if self.minimum < x < self.medium:
            return up(x, self.minimum, self.medium)
        elif self.medium < x < self.maximum:
            return down(x, self.medium, self.maximum)
        elif x == self.medium:
            return 1
        else:
            return 0

    def tinggi(self, x):
        if x <= self.medium:
            return 0
        elif x >= self.maximum:
            return 1
        
        else:
            return up(x, self.medium, self.maximum)

class Debit():
    minimum = 2
    maximum = 4
    
    def lambat(self, α):
        if α >= self.maximum:
            return 0
        elif α <= self.minimum:
            return 1

    def cepat(self, α):
        if α <= self.minimum:
            return 0
        elif α >= self.maximum:
            return 1

    # 2 permintaan 3 persediaan
    def inferensi(self, minyak, jumlah_mesin):
        myk = Minyak()
        msn = Mesin()
        result = []
        
        # [R1] Jika Minyak SEDIKIT, dan Mesin RENDAH, 
        #     MAKA Debit = 2
        α1 = min(myk.sedikit(jumlah_Minyak), msn.rendah(jumlah_mesin))
        z1 = self.minimum
        result.append((α1, z1))

        # [R2] Jika Minyak SEDIKIT, dan Mesin SEDANG, 
        #     MAKA Debit = 10 * jumlah_mesin + 100
        α2 = min(myk.sedikit(jumlah_Minyak), msn.sedang(jumlah_mesin))
        z2 = 10 * jumlah_mesin + 100
        result.append((α2, z2))
        
        # [R3] Jika Minyak SEDIKIT, dan Mesin TINGGI, 
        #     MAKA Debit = 10 * jumlah_mesin + 200
        α3 = min(myk.sedikit(jumlah_Minyak), msn.tinggi(jumlah_mesin))
        z3 = 10 * jumlah_mesin + 200
        result.append((α3, z3))

        # [R4] Jika Minyak BANYAK, dan Mesin RENDAH,
        #     MAKA Debit = 5 * jumlah_Minyak + 2 * jumlah_mesin
        α4 = min(myk.banyak(jumlah_Minyak), msn.rendah(jumlah_mesin))
        z4 = 5 * jumlah_Minyak + 2 * jumlah_mesin
        result.append((α4, z4))

        # [R5] Jika Minyak BANYAK, dan Mesin SEDANG,
        #     MAKA Debit = 5 * jumlah_Minyak + 4 * jumlah_mesin + 100
        α5 = min(myk.banyak(jumlah_Minyak), msn.sedang(jumlah_mesin))
        z5 = 5 * jumlah_Minyak + 4 * jumlah_mesin + 100
        result.append((α5, z5))

        # [R6] Jika Minyak BANYAK, dan Mesin TINGGI,
        #     MAKA Debit = 5 * jumlah_Minyak + 5 * jumlah_mesin + 300
        α6 = min(myk.banyak(jumlah_Minyak), msn.tinggi(jumlah_mesin))
        z6 = 5 * jumlah_Minyak + 5 * jumlah_mesin + 300
        result.append((α6, z6))

        return result
    
    def defuzifikasi(self, jumlah_Minyak, jumlah_mesin):
        inferensi_values = self.inferensi(jumlah_Minyak, jumlah_mesin)
        return sum([(value[0]* value[1]) for value in inferensi_values]) / sum([value[0] for value in inferensi_values])
