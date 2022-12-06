import unittest
from generators.races import Races


class TestRaces(unittest.TestCase):
    def setUp(self):
        self.testrace = Races()
        self.racelist = ["Altmer / High Elf", "Argonian", "Bosmer / Wood Elf",
                         "Breton", "Dunmer / Dark Elf", "Imperial", "Khajiit", "Nord",
                         "Orsimer / Orc", "Redguard"]

    def test_constructor_creates_right_races(self):
        val = self.testrace._races
        self.assertEqual(val, self.racelist)

    def test_generate_race_works(self):
        val = self.testrace.generate_race()
        self.assertIn(val, self.racelist)
