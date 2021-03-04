import unittest

from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):
    
    def setUp(self):
        self.phonebook = PhoneBook()

    def test_lookup_by_name(self):
        self.phonebook.add('Bob','12345')
        number = self.phonebook.lookup('Bob')
        self.assertEqual(number,'12345')

    def test_missing_name_raises_error(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing_name')
    
    # @unittest.skip('WIP')
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_with_different_entries(self):
        self.phonebook.add('Bob','12345')
        self.phonebook.add('Anna','012345')
        self.assertTrue(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_entries(self):
        self.phonebook.add('Bob','12345')
        self.phonebook.add('Sue','12345')
        self.assertFalse(self.phonebook.is_consistent())

    def test_inconsistent_with_duplicate_prefix(self):
        self.phonebook.add('Sue','123')
        self.phonebook.add('Bob','12345')
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_add_names_and_numbers(self):
        self.phonebook.add('Sue','12345')
        self.assertIn('Sue',self.phonebook.get_names())
        self.assertIn('123343',self.phonebook.get_numbers())
