class pesawat:
  def __init__(self,interior, warna, harga):
    self.interior_pesawat  = interior
    self.warna_pesawat  = warna
    self.harga_pesawat  = harga

  def deskripsi(self):
    print("\nspesifikasi pesawat: ")
    print(f"jumlah kursi: {self.interior_pesawat} kursi\nwarna pesawat: {self.warna_pesawat}\nharga pesawat: {self.harga_pesawat}")

class smallJet(pesawat):
  def __init__(self, interior, warna, harga):
      super().__init__(interior, warna, harga)

class mediumJet(pesawat):
  def __init__(self, interior, warna, harga):
      super().__init__(interior, warna, harga)

class largeJet(pesawat):
  def __init__(self, interior, warna, harga):
      super().__init__(interior, warna, harga)

class luxuryJet(pesawat):
  def __init__(self, interior, warna, harga):
      super().__init__(interior, warna, harga)

