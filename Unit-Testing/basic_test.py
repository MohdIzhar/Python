import unittest 
import os

def analyze_text(filename):
    """
    Args:
        filename: The name of file to analyze
    Raises:
        IOError: If file doesn't exist or can't be read
    Returns:
        A tuple where the first element is the number of lines
        in the file and second element is number of characters
        in the file.
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)

    return (lines, chars)

class TextAnalysisTests(unittest.TestCase):
    """Tests for the "analyze_text()" function."""

    def setUp(self):
        """ Fixture that creates the file for the text method to use."""
        self.filename = 'text_analysis_file.txt'
        with open(self.filename,'w') as f:
            f.write('Now we are engaged in great civil war, \n'
                    'Testing whether that nation, \n'
                    'or any nation so concieved and so dedicated,\n'
                    'can long endure.')

    def test_function_runs(self):
        analyze_text(self.filename)

    def test_line_count(self):
        """Check line count is correct."""
        self.assertEqual(analyze_text(self.filename)[0],4)

    def test_character_count(self):
        """Check character count is correct."""
        self.assertEqual(analyze_text(self.filename)[1],131)

    def test_no_such_file(self):
        """Check the proper excetion is thrown for missing file."""
        with self.assertRaises(IOError):
            analyze_text('foobar.txt')

    def test_no_deletion(self):
        """Check that function doesn't delete the file."""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

    def tearDown(self):
        """Fixture that deletes the files used by test methods."""
        try:
            os.remove(self.filename)
        except:
            pass

if __name__ == '__main__':
    unittest.main()