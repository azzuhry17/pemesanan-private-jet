class customer:
  def __init__(self, nama, email, phone, payment, delivery, jet):
    self.nama_cust  = nama
    self.email_cust = email
    self.phone_cust = phone
    self.payment_cust = payment
    self.delivery_method = delivery
    self.jet_order  = jet

  def order(self):
    print(f"\n===== purchase order number {self.phone_cust} =====")
    print(f"\nnama pemesan: {self.nama_cust},\nemail: {self.email_cust} \nnomor handphone: {self.phone_cust} \nmetode pembayaran: {self.payment_cust} \nmetode pengiriman: {self.delivery_method} \njenis pesawat: {self.jet_order}")

class regularCustomer(customer):
  def __init__(self, nama, email, phone, payment, delivery, jet):
      super().__init__(nama, email, phone, payment, delivery, jet)

  def order(self):
      return super().order()

class vipCustomer(customer):
  def __init__(self, nama, email, phone, payment, delivery, jet ,vip):
      super().__init__(nama, email, phone, payment, delivery, jet)
      self.vip_card = vip 

  def order(self):
    print(f"\n===== vip order number {self.phone_cust}{self.vip_card} =====")
    print(f"\nnama pemesan: {self.nama_cust} \nemail: {self.email_cust} \nnomor handphone: {self.phone_cust} \nmetode pembayaran: {self.payment_cust} \nmetode pengiriman: {self.delivery_method} \nnomor kartu: {self.vip_card} \njenis pesawat: {self.jet_order}")