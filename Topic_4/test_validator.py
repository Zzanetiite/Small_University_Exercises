import unittest

from validator import Validator


class TestValidator(unittest.TestCase):
    # By this can remove validator = Validator()
    # and add self. in front of result
    def setUp(self):
        self.validator = Validator()

    def test_it_will_reject_username_if_too_long(self):
        # Assume
        username = 'InvalidTooLong'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_it_will_reject_username_if_white_space_present(self):
        # Assume
        username = 'Re val'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_will_reject_username_if_there_is_no_uppercase_char(self):
        # Assume
        username = 'reval'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertFalse(result)

    def test_will_accept_a_valid_username(self):
        # Assume
        username = 'Reval'

        # Action
        result = self.validator.username_is_valid(username)

        # Assert
        self.assertTrue(result)


# this runs the test automatically
if __name__ == '__main__':
    unittest.main()