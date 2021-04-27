# Imagine a game with one or more rats can attack a player. each individual rat
# has an initial attack value of 1. However, rats attack as a swarm so each rat’s
# attack value is actually equal to the total number of rats in play.
# Given that a rat enters play through the initializer and leave play (dies)
# via its __exit__ method, please implement the Game and Rat classes so that at,
# any point in the game the attack value of a rat is always consistent.



from unittest import TestCase

# class Event(list):
#     def __call__(self, *args, **kwargs):
#         for item in self:
#             item(*args, **kwargs)

class Game:
    def __init__(self):
        self.rats = []

    def subscribe(self, observer):
        self.rats.append(observer)
        self.notify()

    def unsubscribe(self, observer):
        self.rats.remove(observer)
        self.notify()

    def notify(self):
        for observer in self.rats:
            observer.update_attack_value()

class Rat:
    def __init__(self, game):
        self.game = game
        self.attack = 1
        game.subscribe(self)

    def rat_dies(self):
        self.game.unsubscribe(self)

    def update_attack_value(self):
        self.attack = len(self.game.rats)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.rat_dies()

class Evaluate(TestCase):
    def test_single_rat(self):
        game = Game()
        rat = Rat(game)
        self.assertEqual(1, rat.attack)

    def test_two_rats(self):
        game = Game()
        rat = Rat(game)
        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

    def test_three_rats_one_dies(self):
        game = Game()

        rat = Rat(game)
        self.assertEqual(1, rat.attack)

        rat2 = Rat(game)
        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)

        with Rat(game) as rat3:
            self.assertEqual(3, rat.attack)
            self.assertEqual(3, rat2.attack)
            self.assertEqual(3, rat3.attack)

        self.assertEqual(2, rat.attack)
        self.assertEqual(2, rat2.attack)
