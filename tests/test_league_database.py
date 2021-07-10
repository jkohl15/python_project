import unittest
from module6.team_member import TeamMember
from module6.team import Team
from module6.league_database import LeagueDatabase
from module6.competition import Competition
from module6.league import League

class LeagueDatabaseTests(unittest.TestCase):
    # I made a single file called "firstfile.dat" that contains a pickled _sole_instance.
    # I will use this file "firstfile.dat" to test bringing in data from files.
    # This file "firstfile.dat" will never be re-written or re-saved so I can re-use it in multiple tests without changing it.

    def test_load_leaguedatabase(self):
        LeagueDatabase.load("firstfile.dat")
        size_of_league = len(LeagueDatabase._sole_instance.leagues)
        self.assertEqual(1, size_of_league)

        # # THIS WAS THE CODE USED TO CREATE THE SINGLE FILE "firstfile.dat" that is used in subsequent tests
        # a = LeagueDatabase.instance()
        # t1 = TeamMember(1, "Jeff Kohl", "jeffreyalankohl89@gmail.com")
        # t2 = TeamMember(2, "Jeff Kohl 2", "jak0097@auburn.edu")
        # team1 = Team(1, "Team 1")
        # team2 = Team(2, "Team 2")
        # team1.add_member(t1)
        # team2.add_member(t2)
        # comp = Competition(1, [team1, team2], "Here", None)
        # league1 = League(1, "First League")
        # league1.add_team(team1)
        # league1.add_team(team2)
        # league1.add_competition(comp)
        # a.add_league(league1)
        # a.save("firstfile.dat")

    def test_create_leaguedatabase_without_using_sole_instance(self):

        # "a" does NOT use LeagueDatabase.instance()
        a = LeagueDatabase()

        t1 = TeamMember(1, "Jeff Kohl", "jeffreyalankohl89@gmail.com")
        t2 = TeamMember(2, "Jeff Kohl 2", "jak0097@auburn.edu")
        team1 = Team(1, "Team 1")
        team2 = Team(2, "Team 2")
        team1.add_member(t1)
        team2.add_member(t2)
        comp = Competition(1, [team1, team2], "Here", None)
        league1 = League(1, "First League")
        league1.add_team(team1)
        league1.add_team(team2)
        league1.add_competition(comp)
        a.add_league(league1)
        size_of_league = len(a.leagues)
        self.assertEqual(1, size_of_league)

    def test_import_file(self):
        LeagueDatabase.instance().load("firstfile.dat")
        LeagueDatabase._sole_instance.import_league("League Import", "Teams.csv")
        size_of_league = len(LeagueDatabase._sole_instance.leagues)
        self.assertEqual(2, size_of_league)

    def test_import_file_with_duplicate_email_addresses_for_team_members(self):
        LeagueDatabase.instance().load("firstfile.dat")
        LeagueDatabase._sole_instance.import_league("League Import", "Teams2.csv")
        size_of_league = len(LeagueDatabase._sole_instance.leagues)
        self.assertEqual(1, size_of_league)

    def test_import_nonexistent_file(self):
        LeagueDatabase.instance().load("firstfile.dat")
        LeagueDatabase._sole_instance.import_league("League BadImport", "Teams000.csv")
        size_of_league = len(LeagueDatabase._sole_instance.leagues)
        self.assertEqual(1, size_of_league)







