def validate_integer(
        arg_name, arg_value, min_value=None, max_value=None,
        custom_min_message=None, custom_max_message=None,
):
    # Helper function with optional custom messages
    if not isinstance(arg_value, int):
        raise TypeError(f'{arg_name} must be a integer')
    if min_value is not None and arg_value < min_value:
        raise ValueError(f'{arg_name} cannot be less than {min_value}')
    if max_value is not None and arg_value > max_value:
        raise ValueError(f'{arg_name} cannot be greater than {max_value}')


def validate_string(arg_name, arg_value):
    if not isinstance(arg_value, str):
        raise TypeError(f'{arg_name} must be a string')


class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        validate_string('Name', name)
        validate_string('Manufacturer', manufacturer)
        validate_integer('Total', total, min_value=0)
        validate_integer(
            'Allocated', allocated, 0, total,
            custom_max_message='Allocated cannot be greater than total',
        )
        self._total = total
        self._name = name
        self._manufacturer = manufacturer
        self._allocated = allocated

        # Use for child class repr method
        self._resource_repr = \
            (self.__class__.__name__,
             self.name, self.manufacturer, self.total, self.allocated)

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def available(self):
        return self.total - self.allocated

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return '{0}({1}, {2}, {3}, {4})'.format(*self._resource_repr)

    def claim(self, n):
        validate_integer('claim unit(s)', n, 0, self.available)
        self._allocated += n

    def freeup(self, n):
        validate_integer('return', n, 0, self.allocated)
        self._allocated -= n

    def died(self, n):
        validate_integer(
            'broken', n, 0, self.allocated,
        )
        self._allocated -= n
        self._total -= n

    def purchased(self, n):
        validate_integer(
            'purchased', n, 0,
        )
        self._total += n

    def category(self):
        return self.__class__.__name__.lower()


class CPU(Resource):
    def __init__(
            self, name, manufacturer, total, allocated,
            socket, cores, power_watts
    ):
        super().__init__(name, manufacturer, total, allocated)

        validate_string('Socket', socket)
        validate_integer('Cores', cores)
        validate_integer('Power_watts', power_watts)

        self._socket = socket
        self._cores = cores
        self._power_watts = power_watts

        self._CPU_repr = (
            *self._resource_repr,
            self.socket, self.cores, self.power_watts
        )

    @property
    def socket(self):
        return self._socket

    @property
    def cores(self):
        return self._cores

    @property
    def power_watts(self):
        return self._power_watts

    def __repr__(self):
        return '{0}({1}, {2}, {3}, {4}, {5}, {6}, {7})'\
            .format(*self._CPU_repr)


class Storage(Resource):
    def __init__(
            self, name, manufacturer, total, allocated,
            capacity_GB,
    ):
        super().__init__(name, manufacturer, total, allocated)

        validate_integer('Capacity_GB', capacity_GB)
        self._capacity_GB = capacity_GB

        self._storage_repr = (*self._resource_repr, self.capacity_GB)

    @property
    def capacity_GB(self):
        return self._capacity_GB

    def __repr__(self):
        return '{0}({1}, {2}, {3}, {4}, {5})'.format(*self._storage_repr)


class SSD(Storage):
    def __init__(
            self, name, manufacturer, total, allocated,
            capacity_GB,
            interface
    ):
        super().__init__(
            self, name, manufacturer, total, allocated,
            capacity_GB,
        )
        validate_string('Interface', interface)
        self._interface = interface

        self._SSD_repr = (*self._storage_repr, self.interface)

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        return '{0}({1}, {2}, {3}, {4}, {5}, {6})'.format(*self._SSD_repr)


class HDD(Storage):
    def __init__(
            self, name, manufacturer, total, allocated,
            capacity_GB,
            size, rpm
    ):
        super().__init__(
            self, name, manufacturer, total, allocated,
            capacity_GB,
        )
        validate_string('Size', size)
        if size not in ('2.5"', '3.5"'):
            raise ValueError('Expect 2.5" or 3.5" for size')
        self._size = size

        validate_integer('rpm', rpm, 1000, 8000)
        self._rpm = rpm

        self._HDD_repr = (*self._storage_repr, self.size, self.rpm)

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        return '{0}({1}, {2}, {3}, {4}, {5}, {6}, {7})'.format(*self._HDD_repr)
