from tests.base_tests import AppBaseTest


class TestNumbers(AppBaseTest):
    def test_should_return_true_when_number_is_less_than_min_length(self):
        name = 'na'

        self.v.has_min(len(name), 3, 'Name should be at least 3 characters.')
        self.assertTrue(self.v.invalid)

    def test_should_return_true_when_number_is_greater_than_max_length(self):
        name = 'nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'

        self.v.has_max(len(name), 20, 'Name should be max 20 characters')
        self.assertTrue(self.v.invalid)
