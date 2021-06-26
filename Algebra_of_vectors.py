from math import sqrt
from math import pi
from math import acos



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

    def is_parallel_to(self, v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi)
    def is_orthogonal(self, v, tolerance=1e-10):
        return abs(self.dot_product(v) < tolerance)
    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def area_of_a_triangle(self, v):
        return self.area_of_parallelogram/ 2

    def component_parallel_to(self,basis):
        try:
            u = basis.normalizer()
            weight = self.dot_product(u)
            return u.scalar(weight)
        except Exception as e:
            if str(e) == self.CAN_NOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e

    def component_orthogonal_to(self,basis):
        try:
         projection = self.component_parallel_to(basis)
         return self.sub(projection)

        except Exception as e :
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e

    def area_of_parallelogram(self,v):
        cross_parel = self.cross(v)
        return cross_parel.magnitude()

    def cross(self, v):
        try:
            x_1, y_1, z_1 = self.coordinates
            x_2, y_2, z_2 = v.coordinates
            new_coordinates = [y_1 * z_2 - y_2 * z_1,
                               (-(x_1 * z_2 - x_2 * z_1)),
                               x_1 * y_2 - x_2 * y_1]
            return (new_coordinates)
        except ValueError as e:
            msg = str(e)
            if msg == "needs more than two values to unpack":
                self_embedded_in_R3 = Vector(self.coordinates + ("0"))
                v_embedded_in_R3 = Vector(v.coordinates + ("0"))
                return self.embedded_in_R3.cross(v.embedded_in_R3)
            elif (msg == "some many values to unpack" or "needs more than one value to unpack"):
                raise Exception("SELF_ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG")
            else:
                raise e

    def magnitude(self):
        mag = [x * x for x in self.coordinates]
        return sqrt(sum(mag))



    def normalizer(self):
        try:
            magnitude = self.magnitude()
            return self.scalar(1./ magnitude)

        except ZeroDivisionError:
            raise Exception("zero vector can not be normalized")

    def dot_product(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])


    def angle_with(self, v, in_degree=False):
        try:
            u1 = self.normalizer()
            u2 = v.normalizer()
            angle_in_radian = acos(u1.dot_product(u2))
            if in_degree:
                angle_per_radian = 180. / pi
                return angle_per_radian * angle_per_radian
            else:
                return angle_in_radian
        except Exception as e:
            if str(e) == self.CAN_NOT_NORMALIZE_A_ZERO_VECTOR_MSG:
                raise Exception("CAN NOT COMPUTE THE ANGLE OF A ZERO VECTOR")
            else:
                raise e

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

    def scalar(self, number):
        mult = [x * number for x in self.coordinates]
        return mult

v5 = Vector([8.831,-1.331,-6.247])
v = Vector([7.887, 4.138])
v1 = Vector([-8.802, 6.776])
w = Vector([3.183, -7.627])
w1 = Vector([-2.668, 5.319])
vector0 = Vector([2, 4, 5])
vector1 = Vector([1, 0, 0])
v = Vector([4.5, 7])
W = Vector([3, 3.5, 8])
print(v.add(W))
print(v.sub(W))
print(v.scalar(5.98))
print(v.magnitude())
print(v5.normalizer())
print(v.dot_product((v1)))
print("is orthogonal %s:" % v1.is_orthogonal(w))
