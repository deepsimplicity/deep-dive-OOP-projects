class BaseValidator:
    def __init__(self, mini_=None, max_=None):
        self._mini = mini_
        self._max = max_

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)


class IntegerField(BaseValidator):
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f'{self.name} must be an integer')
        elif self._mini is not None and value <= self._mini:
            raise ValueError\
                (f'{self.name} must be greater than {self._mini}')
        elif self._max is not None and value >= self._max:
            raise ValueError\
                (f'{self.name} must be less than {self._max}')
        else:
            instance.__dict__[self.name] = value


class CharField(BaseValidator):
    def __init__(self, mini_, max_):
        mini_ = mini_ or 0
        mini_ = max(mini_, 0)
        super().__init__(mini_, max_)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f'{self.name} must be a string')
        elif self._mini is not None and len(value) <= self._mini:
            raise ValueError\
                (f'{self.name} must be greater than {self._mini} chars')
        elif self._max is not None and len(value) >= self._max:
            raise ValueError\
                (f'{self.name} must be less than {self._max} chars')
        else:
            instance.__dict__[self.name] = value


class Person:
    name = CharField(1, 50)
    age = IntegerField(0, 100)
