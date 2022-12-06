import unittest
from generators.classes import Classes


class TestClasses(unittest.TestCase):
    def setUp(self):
        self.testclass = Classes()
        self.classlist = ["Two-Handed Warrior", "Battlemage", "One-Handed Warrior",
                          "Stealth Archer", "Assassin", "Berserker", "Night Blade"]

    def test_constructor_creates_right_classes(self):
        val = self.testclass.list_classes()
        self.assertEqual(val, self.classlist)

    def test_generate_class_works(self):
        val = self.testclass.generate_class()
        self.assertIn(val, self.classlist)
