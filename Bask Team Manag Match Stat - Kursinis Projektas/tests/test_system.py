import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest

from factory.person_factory import PersonFactory
from models.team import Team
from models.match import Match
from models.stats_record import StatsRecord
from services.file_manager import FileManager


class TestSystem(unittest.TestCase):

    def test_factory_creates_player(self):
        player = PersonFactory.create_person("player", "Test Player", 20, 7, "Guard", 190)
        self.assertEqual(player.name, "Test Player")

    def test_factory_creates_coach(self):
        coach = PersonFactory.create_person("coach", "Test Coach", 50, 20)
        self.assertEqual(coach.name, "Test Coach")

    def test_team_add_player(self):
        coach = PersonFactory.create_person("coach", "Coach", 50, 20)
        team = Team("TestTeam", coach)

        player = PersonFactory.create_person("player", "Player1", 20, 7, "Guard", 190)
        team.add_player(player)

        self.assertEqual(len(team.players), 1)

    def test_team_remove_player(self):
        coach = PersonFactory.create_person("coach", "Coach", 50, 20)
        team = Team("TestTeam", coach)

        player = PersonFactory.create_person("player", "Player1", 20, 7, "Guard", 190)
        team.add_player(player)

        result = team.remove_player(7)

        self.assertEqual(result, "Player removed")
        self.assertEqual(len(team.players), 0)

    def test_team_to_dict(self):
        coach = PersonFactory.create_person("coach", "Coach", 50, 20)
        team = Team("TestTeam", coach)

        player = PersonFactory.create_person("player", "Player1", 20, 7, "Guard", 190)
        team.add_player(player)

        data = team.to_dict()

        self.assertEqual(data["name"], "TestTeam")
        self.assertEqual(data["players"][0]["name"], "Player1")

    def test_match_score(self):
        coach1 = PersonFactory.create_person("coach", "Coach1", 50, 20)
        coach2 = PersonFactory.create_person("coach", "Coach2", 45, 15)

        team1 = Team("Team1", coach1)
        team2 = Team("Team2", coach2)

        match = Match(team1, team2)
        match.set_score(80, 70)

        self.assertEqual(match.score1, 80)
        self.assertEqual(match.score2, 70)

    def test_match_stats(self):
        coach = PersonFactory.create_person("coach", "Coach", 50, 20)
        team = Team("Team", coach)

        player = PersonFactory.create_person("player", "Player1", 20, 7, "Guard", 190)
        team.add_player(player)

        match = Match(team, team)

        stat = StatsRecord(player, 20, 5, 7)
        match.add_stat(stat)

        self.assertEqual(len(match.stats), 1)

    def test_file_save_and_load(self):
        coach = PersonFactory.create_person("coach", "Coach", 50, 20)
        team = Team("TestTeam", coach)

        player = PersonFactory.create_person("player", "Player1", 20, 7, "Guard", 190)
        team.add_player(player)

        filename = "test.json"

        FileManager.save_to_file(team.to_dict(), filename)
        data = FileManager.load_from_file(filename)

        self.assertEqual(data["name"], "TestTeam")

        if os.path.exists(filename):
            os.remove(filename)


if __name__ == "__main__":
    unittest.main()
