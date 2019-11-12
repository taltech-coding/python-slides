class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def name(self):
        # some optional calculation for name
        return f"{self.firstname} {self.lastname}"

    @name.setter
    def name(self, name):
        # some optional validation
        self.firstname, self.lastname = name.split(" ")


if __name__ == '__main__':
    s = Student("Ago", "Luberg")
    s.name = "Ain Kaasik"
    print(s.name)