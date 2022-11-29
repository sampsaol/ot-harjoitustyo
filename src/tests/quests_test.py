import unittest
from quests import Quests


class TestQuests(unittest.TestCase):
    def setUp(self):
        self.classlist = ["Two-Handed Warrior", "Battlemage", "One-Handed Warrior",
                          "Stealth Archer", "Assassin", "Berserker", "Night Blade"]
        self.questlist = ["Dark Brotherhood", "The Companions",
                          "The Thieves Guild", "The College of Winterhold"]

    def test_constructor_creates_correct_list(self):
        quest = Quests(self.classlist[0])
        self.assertEqual(quest._questlines, self.questlist)

    def test_constructor_creates_correct_class(self):
        quest = Quests(self.classlist[0])
        self.assertEqual(quest._class, self.classlist[0])

    def test_primary_questline_works(self):
        testlist = []
        for i in self.classlist:
            quest = Quests(i).primary_questline()
            testlist.append(quest)

        self.assertEqual(testlist, [self.questlist[1], self.questlist[3], self.questlist[1],
                         self.questlist[2], self.questlist[0], self.questlist[1], self.questlist[0]])
