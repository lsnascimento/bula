from unittest import TestCase
from validator import Validator


class AppBaseTest(TestCase):
    def setUp(self):
        self.v = Validator()
