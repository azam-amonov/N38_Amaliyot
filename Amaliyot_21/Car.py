class Car:
    def __init__(self, brand, name, price, speed):
        self.brand = brand
        self.name = name
        self.price = price
        self.speed = speed

    def get(self):
        return (self.brand,
                self.name,
                self.price,
                self.speed)


if __name__ == "__main__":
    car = Car("BMW", "X6", 60000, 230)
    car1 = Car("Mers", "AMG", 70000, 200)
    car2 = Car("Ford", "Mustang", 50000, 250)
    car3 = Car("Ravon", "Gentra", 16000, 160)

    print(car.name, car.brand, car.price, car.speed)
    print(car1.get())

