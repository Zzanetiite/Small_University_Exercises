import unittest
import SecondsToWords


def test_text_is_correct(self):
    self.assertTrue(SecondsToWords.get_time_in_words(3701), '1 hours, 1 minute and 41 seconds')



# this runs the test automatically
if __name__ == '__main__':
    unittest.main()