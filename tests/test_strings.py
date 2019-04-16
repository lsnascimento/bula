from tests.base_tests import AppBaseTest
from validation.schema import schema_name


class TestStrings(AppBaseTest):
    def test_should_return_true_when_string_isnull(self):
        name = None

        self.v.is_notnull_or_notempty(name, schema_name['required'])
        self.assertTrue(self.v.is_invalid)

    def test_should_return_true_when_string_empty(self):
        name = ''

        self.v.is_notnull_or_notempty(name, schema_name['required'])
        self.assertTrue(self.v.is_invalid)
