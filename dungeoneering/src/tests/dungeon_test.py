import unittest
from dungeon import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_constructor_works(self):
        self.assertEqual(f"{self.game.width} {self.game.height} {self.game.scale}", "900 1000 75")
    
    def test_pictures_load(self):
        self.assertEqual(len(self.game.pictures), 5)

    def test_game_launches(self):
        self.game.level_generator()
        self.assertEqual(self.game.level, 1)

    def test_level_changes(self):
        self.game.level_generator()
        self.game.level_generator()
        self.game.level_generator()
        self.assertEqual(self.game.difficulty, 3)

    def test_movement_works(self):
        self.game.level_generator()
        self.game.move(0, 1, False)
        self.assertEqual((self.game.map[-1][0], self.game.map[-1][1]), (0, 3))

    def test_attacking_limiter_works(self):
        self.game.level_generator()
        self.game.move(0, 0, True)
        self.assertEqual(self.game.attacks, 4)

    def test_attacking_works(self):
        self.game.level_generator()
        self.game.map[-2][0] = 4
        self.game.move(0, 0, True)
        self.assertEqual(self.game.map[-2][0], 0)

    def test_moving_beats_monsters(self):
        self.game.level_generator()
        self.game.map[-1][1] = 4
        self.game.move(0, 1, False)
        self.assertEqual((self.game.map[-1][1], self.game.health), (3, 2))