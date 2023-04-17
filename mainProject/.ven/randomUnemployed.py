import random
from packages.Employee import Developer, QA


def randomUnemployed():

    names = ['Bob', 'Nik', 'Fred']

    dev = Developer(random.choice(names), random.randint(18, 80))
    qa = QA(random.choice(names), random.randint(18, 80))

    print(dev.getEmployee())
    print(qa.getEmployee())

    luser = random.choice([dev, qa])

    if luser == dev:

        luser.changeUnemployed()
        print(f"Developer {luser.getEmployee()}")

    else:
        luser.changeUnemployed()
        print(f"QA {luser.getEmployee()}")

