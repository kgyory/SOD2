# bitte implementieren sie ein PersonFactory, die eine nicht-statische create_person() Methode hat, die
#  einen Namen als Paramater nimmt und returniert ein Person-Objekt mit den Namen und ID

from unittest import TestCase
import copy


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    idcounter = 0

    def create_person(self, name):
        p = Person(PersonFactory.idcounter, name)
        PersonFactory.idcounter += 1
        return p


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# Implementiere bitte Line.deep_copy() um eine "Deep Copy" vom Line Objekt zu machen

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        result = copy.deepcopy(self)
        return result


class Evaluate(TestCase):
    def test_exercise_deep_copy(self):
        line1 = Line(
            Point(3, 3),
            Point(10, 10)
        )
        line2 = line1.deep_copy()
        line1.start.x = line1.end.x = line1.start.y = line1.end.y = 0

        self.assertEqual(3, line2.start.x)
        self.assertEqual(3, line2.start.y)
        self.assertEqual(10, line2.end.x)
        self.assertEqual(10, line2.end.y)

    def test_exercise_person(self):
        pf = PersonFactory()

        p1 = pf.create_person('Chris')
        self.assertEqual(p1.name, 'Chris')
        self.assertEqual(p1.id, 0)

        p2 = pf.create_person('Sarah')
        self.assertEqual(p2.id, 1)
