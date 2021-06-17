class CreditCard:
    def __init__(self, pelanggan, bank, akun, limit):
        self.akun = akun
        self.pelanggan = pelanggan
        self.bank = bank
        self.limit = limit
        self.balance = 0

    @staticmethod
    def is_numeric(value):
        return type(value) == type(1) or type(value) == type(1.0)

    def get_customer(self):
        return self.pelanggan

    def get_bank(self):
        return self.bank

    def get_account(self):
        return self.akun

    def get_limit(self):
        return self.limit

    def get_balance(self):
        return self.balance

    def charge(self, price):
        if not self.is_numeric(price):
            raise TypeError('price must be int or float')
        if price + self.balance > self.limit:
            return False
        self.balance += price
        return True

    def make_payment(self, amount):
        if not self.is_numeric(amount):
            raise TypeError('price must be int or float')
        self.balance -= amount


if __name__ == '__main__':
    card = CreditCard('Yuyun Rusmianti', 'BRI', '04022002', 100000)
    card.charge(500)
print(card.__dict__)