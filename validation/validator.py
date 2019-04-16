class Emitter:
    def __init__(self):
        self._notifications = []

    @property
    def is_valid(self):
        return len(self.notifications) == 0

    @property
    def is_invalid(self):
        return len(self.notifications) > 0

    @property
    def notifications(self):
        return self._notifications

    @notifications.setter
    def notifications(self, value):
        return self._notifications.append(value)


class Validator(Emitter):
    def __init__(self):
        super().__init__()

    # Strings
    def is_notnull_or_notempty(self, val, message):
        if val is None or val == '':
            self.notifications = message

    def is_null_or_empty(self, val, message):
        if val is not None or val != '':
            self.notifications = message

    def is_equal(self, val1, val2, message):
        if val1 != val2:
            self.notifications = message

    def is_not_equal(self, val1, val2, message):
        if val1 == val2:
            self.notifications = message

    # Numbers
    def has_min(self, val, min, message):
        if val < min:
            self.notifications = message

    def has_max(self, val, max, message):
        if val > max:
            self.notifications = message

    def is_between(self, val, min, max, message):
        if val < min or val > max:
            self.notifications = message

    # Boolean
    def is_true(self, val, message):
        if not val:
            self.notifications = message

    def is_false(self, val, message):
        if val:
            self.notifications = message
