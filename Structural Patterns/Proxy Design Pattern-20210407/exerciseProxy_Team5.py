# You are given the Person class and asked to write a ResponsiblePerson proxy that does the
# following:
# Allows person to drink unless they are Younger than 18 (in that case, return "too Young")
# Allows person to drive unless they are Younger than 16 (otherwise, "too Young")
# In case of driving while drink, returns "dead", regardless of age


from unittest import TestCase


class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person
        self.age = person.age

    def drink(self):
        if self.age >= 18:
            return self.person.drink()
        else:
            return 'too young'

    def drive(self):
        if self.age >= 16:
            return self.person.drive()
        else:
            return 'too young'

    def drink_and_drive(self):
        return 'dead'


class Evaluate(TestCase):
    def test_exercise(self):
        p = Person(10)
        rp = ResponsiblePerson(p)

        self.assertEqual('too young', rp.drive())
        self.assertEqual('too young', rp.drink())
        self.assertEqual('dead', rp.drink_and_drive())

        rp.age = 20

        self.assertEqual('driving', rp.drive())
        self.assertEqual('drinking', rp.drink())
        self.assertEqual('dead', rp.drink_and_drive())
