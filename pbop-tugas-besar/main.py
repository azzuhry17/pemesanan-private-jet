from customer import *
from pesawat import *

privateJet = [
  "private jet kecil", 
  "private jet sedang",
  "private jet besar"
]

vipJets = [
  "private jet kecil", 
  "private jet sedang", 
  "private jet besar",
  "private jet luxury"
]

paymentMethods = [
  "cheque", 
  "credit card", 
]

jetSeats = [
  "10",
  "15",
  "20"
]

jetInterior = [
  "10",
  "15",
  "20",
]

jetColors = [
  "merah",
  "kuning",
  "hijau",
  "biru",
]

jetPrice = [
  "50 milyar",
  "80 milyar",
  "120 milyar",
  "150 milyar",
  "200 milyar",
]

deliveries = [
  "pick up by pilot",
  "deliver to hangar"
]

def jetColorFunc(jetColor):
  if jetColor == "1" or jetColor == 1:
    return jetColors[0]
  elif jetColor == "2" or jetColor == 2:
    return jetColors[1]
  elif jetColor == "3" or jetColor == 3:
    return jetColors[2]
  elif jetColor == "4" or jetColor == 4:
    return jetColors[3]
  else:
    return "input anda salah"

def luxurySeat(customSeat):
  if customSeat == "1" or customSeat == 1:
    return jetInterior[0]
  elif customSeat == "2" or customSeat == 2:
    return jetInterior[1]
  elif customSeat == "3" or customSeat == 3:
    return jetInterior[2]
  else:
    return "input anda salah"

def payment():
  print(f"\n1.{paymentMethods[0]} \n2.{paymentMethods[1]}")
  paymentInput = input("pilih metode pembayaran: ")
  if paymentInput == "1" or paymentInput == 1:
    return "cheque"
  elif paymentInput == "2" or paymentInput == 2:
    return "credit card" 
  else:
    print("metode pembayaran tidak tersedia")

def delivery():
  print(f"\n1.{deliveries[0]} \n2.{deliveries[1]}")
  paymentInput = input("pilih metode pembayaran: ")
  if paymentInput == "1" or paymentInput == 1:
    return "pick up by pilot"
  elif paymentInput == "2" or paymentInput == 2:
    return "deliver to hangar" 
  else:
    print("metode pembayaran tidak tersedia")

def main():
  konfirmasi_pengguna = input("apakah anda pengguna centurion card ? [ Ya / Tidak ]: ")
   
  if konfirmasi_pengguna == "ya" or konfirmasi_pengguna == "Ya":


    nama_pelanggan    = input("masukkan nama anda: ")
    email_pelanggan   = input("masukkan alamat email anda: ")
    telpon_pelanggan  = input("masukkan nomor telpon anda: ")
    card_pelanggan    = input("masukkan nomor visa anda: ")

    print(f"\nprivate jets \n1.{vipJets[0]} \n2.{vipJets[1]} \n3.{vipJets[2]} \n4.{vipJets[3]}")
    aircraftInput = input("\npilih jenis pesawat: ")

    if aircraftInput == "1":
      customerAircraft = vipJets[0]
      jetprice = jetPrice[0]

      print(f"\n1.{jetColors[0]} \n2.{jetColors[1]} \n3.{jetColors[2]} \n4.{jetColors[3]}")
      jetColorInput = input("pilih warna pesawat anda: ")
      vip = vipCustomer(nama_pelanggan, email_pelanggan, 
      telpon_pelanggan, payment(),  delivery(), 
      customerAircraft, card_pelanggan)
      vip.order()
      luxury = smallJet(jetSeats[0], jetColorFunc(jetColorInput), jetprice)
      luxury.deskripsi()

    elif aircraftInput == "2":
      customerAircraft = vipJets[1]
      jetprice = jetPrice[1]

      print(f"\n1.{jetColors[0]} \n2.{jetColors[1]} \n3.{jetColors[2]} \n4.{jetColors[3]}")
      jetColorInput = input("pilih warna pesawat anda: ")
      vip = vipCustomer(nama_pelanggan, email_pelanggan, telpon_pelanggan, payment(), delivery(), customerAircraft, card_pelanggan)
      vip.order()
      luxury = mediumJet(jetSeats[1], jetColorFunc(jetColorInput), jetprice)
      luxury.deskripsi()

    elif aircraftInput == "3":
      customerAircraft = vipJets[2]
      jetprice = jetPrice[2]

      print(f"\n1.{jetColors[0]} \n2.{jetColors[1]} \n3.{jetColors[2]} \n4.{jetColors[3]}")
      jetColorInput = input("pilih warna pesawat anda: ")
      vip = vipCustomer(nama_pelanggan, email_pelanggan, telpon_pelanggan, payment(),delivery(), customerAircraft, card_pelanggan)
      vip.order()
      luxury = largeJet(jetSeats, jetColorFunc(jetColorInput), jetprice)
      luxury.deskripsi()

    elif aircraftInput == "4":
      print(f"\n1.{jetInterior[0]} \n2.{jetInterior[1]} \n3.{jetInterior[2]}")
      seatInput = input("pilih jumlah kursi pesawat : ")
      customerAircraft = vipJets[3]
      jetprice = jetPrice[3]

      print(f"\n1.{jetColors[0]} \n2.{jetColors[1]} \n3.{jetColors[2]} \n4.{jetColors[3]}")
      jetColorInput = input("pilih warna pesawat anda: ")
      vip = vipCustomer(nama_pelanggan, email_pelanggan, telpon_pelanggan, payment(), delivery(), customerAircraft, card_pelanggan)
      vip.order()
      luxury = luxuryJet(luxurySeat(seatInput), jetColorFunc(jetColorInput), jetprice)
      luxury.deskripsi()
    else:
      print("pilihan anda tidak ditemukan")

  elif konfirmasi_pengguna == "tidak" or konfirmasi_pengguna == "Tidak":

    nama_pelanggan    = input("masukkan nama anda: ")
    email_pelanggan   = input("masukkan alamat email anda: ")
    telpon_pelanggan  = input("masukkan nomor telpon anda: ")

    print(f"\nprivate jets \n1.{privateJet[0]} \n2.{privateJet[1]} \n3.{privateJet[2]}")
    aircraftInput = input("\npilih jenis pesawat: ")

    if aircraftInput == "1":
      customerAircraft = privateJet[0]
      jetseat = jetSeats[0]
      jetprice = jetPrice[0]

      print(f"\n1.{jetColors[0]} \n2.{jetColors[1]} \n3.{jetColors[2]} \n4.{jetColors[3]}")
      jetColorInput = input("pilih warna pesawat anda: ")
      customer = regularCustomer(nama_pelanggan, email_pelanggan, telpon_pelanggan, payment(), delivery(), customerAircraft)
      customer.order()
      smalljet = smallJet(jetseat, jetColorFunc(jetColorInput), jetprice)
      smalljet.deskripsi()

    elif aircraftInput == "2":
      customerAircraft = privateJet[1]
      jetseat = jetSeats[1]
      jetprice = jetPrice[1]

      print(f"\n1.{jetColors[0]} \n2.{jetColors[1]} \n3.{jetColors[2]} \n4.{jetColors[3]}")
      jetColorInput = input("pilih warna pesawat anda: ")
      customer = regularCustomer(nama_pelanggan, email_pelanggan, telpon_pelanggan, payment(), delivery(), customerAircraft)
      customer.order()
      mediumjet = mediumJet(jetseat, jetColorFunc(jetColorInput), jetprice)
      mediumjet.deskripsi()
    elif aircraftInput == "3":
      customerAircraft = privateJet[2]
      jetseat = jetSeats[2]
      jetprice = jetPrice[2]

      print(f"\n1.{jetColors[0]} \n2.{jetColors[1]} \n3.{jetColors[2]} \n4.{jetColors[3]}")
      jetColorInput = input("pilih warna pesawat anda: ")
      customer = regularCustomer(nama_pelanggan, email_pelanggan, telpon_pelanggan, payment(), delivery(), customerAircraft)
      customer.order()
      largejet = largeJet(jetseat, jetColorFunc(jetColorInput), jetprice)
      largejet.deskripsi()
    else:
      print("pilihan anda tidak ditemukan")
  else:
    print("input anda salah")
main()