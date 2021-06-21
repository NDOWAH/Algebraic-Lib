class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        except TypeError:
            raise ValueError("The coordinates must be nonempty")
        except TypeError:
            raise ValueError("The coordinate must be an iterable")

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return new_coordinates

    def sub(self, v):
        new_coordinate = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return new_coordinate


v = Vector([4.5, 7])
W = Vector([3, 3.5, 8])
print(v.add(W))
print(v.sub(W))
print(v.scala(5.98))
