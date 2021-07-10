from module6.team import Team
from module6.team_member import TeamMember
from module6.fake_email import FakeEmailer
import unittest
from module6.custom_exceptions import DuplicateOid
from module6.custom_exceptions import DuplicateEmail


class TeamTests(unittest.TestCase):
    # test provided
    def test_create(self):
        name = "Curl Jam"
        oid = 10
        t = Team(oid, name)
        self.assertEqual(name, t.name)
        self.assertEqual(oid, t.oid)

    # test provided
    def test_adding_adds_to_members(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        self.assertIn(tm1, t.members)
        self.assertNotIn(tm2, t.members)
        t.add_member(tm2)
        self.assertIn(tm1, t.members)
        self.assertIn(tm2, t.members)

    # test provided
    def test_removing_removes_from_members(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        t.add_member(tm2)
        t.remove_member(tm1)
        self.assertNotIn(tm1, t.members)
        self.assertIn(tm2, t.members)

    def test_send_email(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f1")
        tm2 = TeamMember(6, "g", "g1")
        t.add_member(tm1)
        t.add_member(tm2)

        fakeemail = FakeEmailer()

        self.assertEqual(t.send_email(fakeemail, "Hello", "Goodbye"), ['f1', 'g1'])
        self.assertEqual((['f1', 'g1'], "Hello", "Goodbye"), fakeemail.messages[0])

    def test_no_teammembers_in_team(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        self.assertEqual(t.remove_member(tm1), None)

    def test_string_override(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        t.add_member(tm2)
        self.assertEqual((str(t)), "Team Flintstones: 2 members")

    def test_add_duplicate_teammember_throw_exception(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(5, "g", "g")
        t.add_member(tm1)
        with self.assertRaises(DuplicateOid):
            t.add_member(tm2)
        self.assertEqual(1, len(t.members))

    def test_add_duplicate_email_throw_exception(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "f", "f")
        t.add_member(tm1)
        with self.assertRaises(DuplicateEmail):
            t.add_member(tm2)
        self.assertEqual(1, len(t.members))