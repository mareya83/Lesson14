class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.unemployed = False

    def changeUnemployed(self):
        self.unemployed = True
        return self.unemployed

    def getEmployee(self):
        return {"Name": self.name,
               "Age": self.age,
               "Unemployed": self.unemployed}


class Developer (Employee):
    def __init__(self, name, age):
        super().__init__(name, age)


class QA(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
