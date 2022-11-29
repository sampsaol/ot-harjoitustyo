import unittest
from character_service import CharacterService


class TestCharacterService(unittest.TestCase):
    def setUp(self):
        self.character = CharacterService()
        self.racelist = ["Altmer / High Elf", "Argonian", "Bosmer / Wood Elf",
                         "Breton", "Dunmer / Dark Elf", "Imperial", "Khajiit", "Nord",
                         "Orsimer / Orc", "Redguard"]
        self.classlist = ["Two-Handed Warrior", "Battlemage", "One-Handed Warrior",
                          "Stealth Archer", "Assassin", "Berserker", "Night Blade"]
        self.questlist = ["Dark Brotherhood", "The Companions",
                          "The Thieves Guild", "The College of Winterhold"]

    def test_constructor_creates_character_list(self):
        characters = self.character.list_generated_characters()
        self.assertEqual(characters, [])

    def test_generating_characters_work(self):
        character = self.character.generate_character()
        self.assertIn(character[0], self.racelist)
        self.assertIn(character[1], self.classlist)
        self.assertIn(character[2], self.questlist)

    def test_generating_characters_save_it_in_character_list(self):
        character = self.character.generate_character()
        self.assertIn(character, self.character.list_generated_characters())
