import unittest
from module6.team_member import TeamMember
from module6.fake_email import FakeEmailer


class TeamMemberTests(unittest.TestCase):
    # provided test
    def test_create(self):
        oid = 1
        name = "Fred"
        email = "fred.flintstone@gmail.com"
        tm = TeamMember(oid, name, email)
        self.assertEqual(oid, tm.oid)
        self.assertEqual(name, tm.name)
        self.assertEqual(email, tm.email)

    # provided test
    def test_equality_based_on_id(self):
        tm_1 = TeamMember(1, "name", "email")
        tm_2 = TeamMember(1, "other name", "other email")
        tm_3 = TeamMember(2, "name", "email")

        # team members must be equal to themselves
        self.assertTrue(tm_1 == tm_1)
        self.assertTrue(tm_2 == tm_2)
        self.assertTrue(tm_3 == tm_3)

        # same id are equal, even if other fields different
        self.assertTrue(tm_1 == tm_2)

        # different ids are not equal, even if other fields the same
        self.assertTrue(tm_1 != tm_3)

    # provided test
    def test_hash_based_on_id(self):
        tm_1 = TeamMember(1, "name", "email")
        tm_2 = TeamMember(1, "other name", "other email")
        tm_3 = TeamMember(2, "name", "email")

        # hash depends only on id
        self.assertTrue(hash(tm_1) == hash(tm_2))

        # objects with different id's may have different hash codes
        # note: this is not a requirement of the hash function but
        # for the case of id == 1 and id == 2 we can verify that their
        # hash codes are different in a REPL (just print(hash(1)) etc).
        self.assertTrue(hash(tm_1) != hash(tm_3))

    def test_send_email(self):
        tm_1 = TeamMember(1, "name", "email")
        fakeemailer = FakeEmailer()
        self.assertEqual(tm_1.send_email(fakeemailer, "Hello", "Goodbye"), "email")
        self.assertEqual((["email"], "Hello", "Goodbye"), fakeemailer.messages[0])
        self.assertEqual(1, len(fakeemailer.messages))

    def test_string_override(self):
        tm_1 = TeamMember(1, "name", "email")
        self.assertEqual(str(tm_1), "Name<Email>")


if __name__ == '__main__':
    unittest.main()
