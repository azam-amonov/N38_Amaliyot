class Person:
    def __init__(self, firstName, lastName, emailAddress):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress

    def __str__(self):
        return f"{self.firstName}, {self.lastName}, {self.emailAddress}"


class Employee(Person):
    def __init__(self, firstName, lastName, emailAddress, experience, salary):
        super(Employee, self).__init__(firstName, lastName, emailAddress)
        self.experience = experience
        self.salary = salary

    def __str__(self):
        return f"{self.firstName}, {self.lastName}, {self.emailAddress}, {self.experience}, {self.salary}"


if __name__ == "__main__":
    person = Person("John", "Doe", "John@gmail.com")
    employee = Employee(person.firstName, person.lastName, person.emailAddress, 5, 1000)
    employee2 = Employee("Anna", "Potter", "annapotter@gmail.com",5, 1000)

    print(person)
    print(employee)
    print(employee2)
