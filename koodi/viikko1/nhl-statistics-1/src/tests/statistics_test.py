from typing import Tuple
import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_statistics_search_true_player(self):
        self.assertIsNot(self.statistics.search('Kurri'),None)
    
    def test_statistics_search_false_player(self):
        self.assertEqual(self.statistics.search('Laine'),None)

    def test_statistics_team(self):
        self.assertEqual(len(self.statistics.team('EDM')),3)
    
    def test_statistics_top_scorers(self):
        self.assertEqual(self.statistics.top_scorers(1)[0].name,'Gretzky')