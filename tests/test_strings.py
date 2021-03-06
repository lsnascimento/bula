from tests.base_tests import AppBaseTest


class TestStrings(AppBaseTest):
    def test_should_return_true_when_string_isnull(self):
        name = None

        self.v.is_notnull_or_notempty(name, 'Name cannot be null or empty')
        self.assertTrue(self.v.invalid)

    def test_should_return_true_when_string_empty(self):
        name = ''

        self.v.is_notnull_or_notempty(name, 'Name cannot be null or empty')
        self.assertTrue(self.v.invalid)
