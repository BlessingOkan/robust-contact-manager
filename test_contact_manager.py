# test_contact_manager.py
import unittest
import contact_manager as cm

class TestContactManager(unittest.TestCase):
    def setUp(self):
        cm.reset_contacts()

    def test_add_contact_success(self):
        self.assertTrue(cm.add_contact("Alice", "555-1234"))
        self.assertEqual(cm.contacts["Alice"], "555-1234")

    def test_find_existing(self):
        cm.add_contact("Bob", "555-2222")
        self.assertEqual(cm.find_contact("Bob"), "555-2222")

    def test_find_missing_returns_none(self):
        self.assertIsNone(cm.find_contact("Nope"))

    def test_delete_existing(self):
        cm.add_contact("Cara", "555-3333")
        self.assertTrue(cm.delete_contact("Cara"))
        self.assertNotIn("Cara", cm.contacts)

    def test_delete_missing(self):
        self.assertFalse(cm.delete_contact("Ghost"))

    def test_add_duplicate_raises(self):
        cm.add_contact("Dana", "555-4444")
        with self.assertRaises(cm.DuplicateContactError):
            cm.add_contact("Dana", "999-9999")

if __name__ == "__main__":
    unittest.main()