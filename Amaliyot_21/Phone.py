class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return (f"Brand: {self.brand}\n"
                f"Name: {self.model}\n"
                f"Price: {self.price}\n$")

    def changePrice(self, newPrice):
        self.price = newPrice


if __name__ == "__main__":
    myPhone = Phone("Nokia", "6300", 100)
    print(myPhone)

    myPhone.changePrice(120)
    print(myPhone)
