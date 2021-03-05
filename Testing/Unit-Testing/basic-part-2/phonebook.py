class PhoneBook:
    """ To store the phone number and name of person
        Phonebook is 
            Consistent when all different.
            Consistent when empty.
            Inconsistent when duplicates.
            Inconsistent when duplicates prefix.
        Ex: emergency - 911
            Bob - 9114567890
            Both are in consistent
    """
    def __init__(self):
        self._numbers = {}

    def add(self, name, number):
        """
        Args:
            name: The person contact name.
            number: The person contact number.

        Returns:
            None
        """
        self._numbers[name] = number

    def lookup(self, name):
        """
        Args:
            name: The name to be search in phonebook
        Returns:
            The number in phonebook.
        """
        return self._numbers[name]

    def is_consistent(self):
        """ Check for unique numbers """
        for name1, number1 in self._numbers.items():
            for name2, number2 in self._numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True
    
