from tests.base_tests import AppBaseTest
from validation.schema import schema_name


class TestNumbers(AppBaseTest):
    def test_should_return_true_when_number_is_less_than_min_length(self):
        name = 'na'

        self.v.has_min(
            len(name),
            schema_name['min']['len'],
            schema_name['min']['message'])

        self.assertTrue(self.v.is_invalid)

    def test_should_return_true_when_number_is_greater_than_max_length(self):
        name = 'nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'

        self.v.has_max(
            len(name),
            schema_name['max']['len'],
            schema_name['max']['message'])

        self.assertTrue(self.v.is_invalid)
