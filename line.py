from decimal import Decimal, getcontext
import vectoralgebra
getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = vectoralgebra(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

        def set_basepoint(self):
            try:
                n = self.normal_vector
                c = self.constant_term
                basepoint_coords = ['0']*self.dimension

                initial_index = Line.first_nonzero_index(n)
                initial_coefficient = n[initial_index]

                basepoint_coords[initial_index] = c/initial_coefficient
                self.basepoint = vectoralgebra(basepoint_coords)

            except Exception as e:
                if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                    self.basepoint = None
                else:
                    raise e