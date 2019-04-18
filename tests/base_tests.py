from unittest import TestCase
from bula.validator import Validator


class AppBaseTest(TestCase):
    def setUp(self):
        self.v = Validator()
