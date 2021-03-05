import pytest, sys
from phonebook import PhoneBook

@pytest.fixture
def phonebook(tmpdir):
    "Provides and empty phonebook"
    return PhoneBook(tmpdir)

def test_lookup_by_name(phonebook):
    phonebook.add('Bob', '1234')
    assert '1234' == phonebook.lookup('Bob')

def test_phonebook_contains_all_names(phonebook):
    phonebook.add('Bob', '1234')
    # assert phonebook.names() == {'Bob', 'Missing'}
    # assert "Missing" in phonebook.names()
    assert "Bob" in phonebook.names()
    
# @pytest.mark.skip('WIP')
@pytest.mark.skipif(sys.version_info < (3,6), reason = "requires python3.6 or higher")
def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('Bob')


