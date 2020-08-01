class Account:
    _interest_rate = 0.005

    def __init__(self, first_name, last_name, acct_num, balance=0):
        for attr in (
                (first_name, 'First name'),
                (last_name, 'Last name'),
                (acct_num, 'Account number'),
        ):
            if not isinstance(attr[0], str):
                raise TypeError(f'{attr[1]} must be a string')

        if balance < 0 or not isinstance(balance, int):
            raise ValueError('Balance must an integer and greater than 0')

        self._first_name = first_name.strip()
        self._last_name = last_name.strip()
        self._acct_num = acct_num
        self._balance = balance
        self._full_name = None

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name('_first_name', value, 'First')
        self._full_name = None

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name('_last_name', value, 'Last')
        self._full_name = None

    @property
    def full_name(self):
        # Full name is cached
        # Only calculate if name(s) change
        if self._full_name is None:
            self._full_name = self.first_name + ' ' + self.last_name
        return self._full_name

    @property
    def balance(self):
        return self._balance

    def validate_and_set_name(self, attr_name, value, field_title):
        if value is None or isinstance(value, str):
            setattr(self, attr_name, value)
        else:
            raise TypeError(f'{field_title} name must be a string')

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, float) or not value > 0:
            raise TypeError\
                ('Interest rate must be a float and greater than 0')
        cls._interest_rate = value

    def deposit(self, value):
        if isinstance(value, int) and value > 0:
            self._balance += value
        else:
            raise ValueError\
                ('Deposit amount must be an integer and greater than 0')

    def withdraw(self, value):
        if isinstance(value, int) and self.balance > value > 0:
            self._balance -= value
        else:
            raise ValueError\
                ('Withdraw amount must be an integer and less than balance')

    def pay_interest(self):
        self._balance += self._balance * Account._interest_rate
