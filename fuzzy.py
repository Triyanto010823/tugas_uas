
class JenisBaju():
    batik = 20
    kemeja = 30
    kaos = 50

    def turun(self, x):
        if x <= self.batik:
            return 0
        elif x >= self.kemeja:
            return 1
        else:
            return bawah(x, self.kemeja, self.batik)

    def pas(self, x):
        if self.batik < x < self.kemeja:
            return atas(x, self.batik, self.kemeja)
        elif self.kemeja < x < self.kaos:
            return bawah(x, self.kemeja, self.kaos)
        elif x == self.kemeja:
            return 1
        else:
            return 0

    def naik(self, x):
        if x >= self.kemeja:
            return 1
        elif x <= self.kaos:
            return 0
        else:
            return up(x, self.kaos, self.kemeja)

class BahanBaju():
    drill = 20
    katun = 40
    denim = 60

    def sedikit(self, x):
        if x >= self.drill:
            return 0
        elif x <= self.katun:
            return 1
        else:
            return down(x, self.katun, self.drill)
    
    def cukup(self, x):
        if self.drill < x < self.katun:
            return up(x, self.drill, self.katun)
        elif self.katun < x < self.denim:
            return down(x, self.katun, self.denim)
        elif x == self.katun:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.denim:
            return 1
        elif x <= self.katun:
            return 0
        else:
            return up(x, self.katun, self.denim)

class WarnaBaju():
    putih = 20
    hitam = 30
    navy = 40

    def sedikit(self, x):
        if x >= self.hitam:
            return 0
        elif x <= self.putih:
            return 1
        else:
            return down(x, self.putih, self.hitam)
    
    def cukup(self, x):
        if self.putih < x < self.hitam:
            return up(x, self.hitam, self.putih)
        elif self.putih < x < self.navy:
            return down(x, self.putih, self.navy)
        elif x == self.putih:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.navy:
            return 1
        elif x <= self.putih:
            return 0
        else:
            return up(x, self.putih, self.pink)

class MotifBaju():
    burung = 30
    badak = 40
    wallet = 50
   
    def sedikit(self, x):
        if x >= self.badak:
            return 0
        elif x <= self.burung:
            return 1
        else:
            return down(x, self.burung, self.badak)
    
    def cukup(self, x):
        if self.burung < x < self.badak:
            return up(x, self.burung, self.)
        elif self.burung < x < self.wallet:
            return down(x, self.badak, self.wallet)
        elif x == self.badak:
            return 1
        else:
            return 0

    def banyak(self, x):
        if x >= self.wallet:
            return 1
        elif x <= self.badak:
            return 0
        else:
            return up(x, self.badak, self.wallet)
