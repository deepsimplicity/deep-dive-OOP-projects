from math import sin, cos, pi


class Polygon:
    def __init__(self, n, R):
        Polygon._validate_field(n, int)
        Polygon._validate_field(R, int)
        if n < 3:
            raise ValueError('Polygon: sides/vertices > 3')

        self._n = n
        self._R = R
        self._vertices = n
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    def __repr__(self):
        return f'Polygon(n={self.edges}, R={self.circumradius})'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.vertices == other.vertices and
                    self.circumradius == other.circumradius)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.vertices > other.vertices
        else:
            return NotImplemented

    def _reset_properties_to_none(self):
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @staticmethod
    def _validate_field(value, type_):
        if not isinstance(value, type_):
            raise TypeError(f'Expect {type_.__name__}, '
                            f'got {type(value).__name__} instead')

    @property
    def edges(self):
        return self._n

    @edges.setter
    def edges(self, value):
        Polygon._validate_field(value, int)
        self._n = value
        self._vertices = value
        Polygon._reset_properties_to_none(self)

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, value):
        Polygon._validate_field(value, int)
        self._vertices = value
        self._n = value
        Polygon._reset_properties_to_none(self)

    @property
    def circumradius(self):
        return self._R

    @circumradius.setter
    def circumradius(self, value):
        Polygon._validate_field(value, int)
        self._R = value
        Polygon._reset_properties_to_none(self)

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle = \
                (self.edges - 2) * (180 / self.edges)
        return self._interior_angle

    @property
    def edge_length(self):
        if self._edge_length is None:
            self._edge_length = \
                2 * self.circumradius * sin(pi / self.edges)
        return self._edge_length

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = \
                self.circumradius * cos(pi / self.edges)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = \
                0.5 * self.edges * self.edge_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = \
                self._n * self.edge_length
        return self._perimeter
