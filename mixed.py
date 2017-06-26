from fractions import Fraction


class Mixed(object):
    """
    Manage mixed numbers.

    >>> mixed = Mixed(3.75)
    >>> mixed
    Mixed(3 + 3/4)
    >>> another = Mixed.float_to_mixed(1.5)
    >>> another
    Mixed(1 + 1/2)
    >>> result = mixed + another
    >>> result
    Mixed(5 + 1/4)
    >>> result.__float__()
    5.25
    """

    def __init__(self, float_, limit_denominator=1000000, use_dash=True):
        self._float = float_
        self._use_dash = use_dash
        self._mix = self._implicit_form(float_, limit_denominator, use_dash)

    def _implicit_form(self, float_, limit_denominator, use_dash):
        if not float_:
            return '-' if use_dash else '0'

        self._int = int(float_)
        self._fract = Fraction(float_ - self._int)

        if limit_denominator:
            self._fract = self._fract.limit_denominator(limit_denominator)

        if self._int and self._fract:
            return '{} {}'.format(self._int, self._fract)
        else:
            return '{}'.format(
                *(filter(None, [self._int, self._fract]))
            )

    def implicit_form(self, use_dash=True):
        """
        Return the implicit form of a mixed number.

        This is a visual way to describe it, formatted like: '2 3/4'.
        Empty values are represented by '-' (default) or '0'.
        """
        if self._use_dash is use_dash:
            return self._mix
        else:
            return '-' if use_dash else '0'

    def explicit_form(self):
        """
        Return the explicit form of a mixed number.

        This is its equivalent mathematical expression, formatted
        like: '2 + 5/11'.
        """
        return self._mix.replace(' ', ' + ') if self._mix != '-' else '0'

    @classmethod
    def float_to_mixed(cls, float_, limit_denominator=1000000):
        """
        Convert given float to mixed number.

        >>> Mixed.float_to_mixed(0)
        Mixed(0)
        >>> Mixed.float_to_mixed(0.3)
        Mixed(3/10)
        >>> Mixed.float_to_mixed(2.25)
        Mixed(2 + 1/4)
        """
        return Mixed(float_, limit_denominator)

    def __str__(self):
        return self._mix

    def __repr__(self):
        return self.__class__.__name__ + '({})'.format(self.explicit_form())

    def __add__(self, another):
        return Mixed(self._float + float(another))

    def __mul__(self, another):
        # TODO: (a + b/c) * (d + e/f) = d *(a + b/c) + e/f *(b/c + a)
        # find a way to multiply for better performance
        return Mixed(self._float * float(another))

    def __sub__(self, another):
        return Mixed(self._float - float(another))

    def __rsub__(self, another):
        return Mixed(float(another) - self._float)

    def __float__(self):
        return float(self._float)

    def __int__(self):
        return int(self._float)

    # commutative operations
    __radd__ = __add__
    __rmul__ = __mul__

    def __bool__(self):
        return not (self._mix == '-' or self._mix == '0')

    __eq__ = lambda self, another: self._float == float(another)  # noqa
    __ne__ = lambda self, another: self._float != float(another)  # noqa
    __lt__ = lambda self, another: self._float < float(another)   # noqa
    __le__ = lambda self, another: self._float <= float(another)  # noqa
    __gt__ = lambda self, another: self._float > float(another)   # noqa
    __ge__ = lambda self, another: self._float >= float(another)  # noqa
    __hash__ = lambda self: hash(self._float)                     # noqa
