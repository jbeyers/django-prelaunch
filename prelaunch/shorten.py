class ShortCode():
    """Translate from a shortcode string to integer and vice versa.

    >>> digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    >>> hex = '0123456789ABCDEF'
    >>> alpha = map(chr, range(97, 123))

    No offset and direct digit substitution should be equal to str
    >>> coder = ShortCode(0, 'abcdgg')
    Traceback (most recent call last):
        ...
    Exception: Duplication in digits is not allowed.

    No offset and direct digit substitution should be equal to str
    >>> coder = ShortCode(0, digits)
    >>> coder.get_shortcode(12345)
    '12345'

    >>> coder.get_number('12345')
    12345

    The offset gets added to the integer.
    >>> coder = ShortCode(100, digits)
    >>> coder.get_shortcode(12345)
    '12445'

    >>> coder.get_number('12345')
    12245

    Using hex digits give us an integer to hex conversion. 
    >>> hexer = ShortCode(0, hex)
    >>> hexer.get_shortcode(255)
    'FF'

    >>> hexer.get_shortcode(256)
    '100'

    >>> alpher = ShortCode(0, alpha)
    >>> alpher.get_shortcode(0)
    'a'

    >>> alpher.get_shortcode(1)
    'b'

    >>> alpher.get_shortcode(25)
    'z'

    >>> alpher.get_shortcode(26)
    'ba'

    """

    def __init__(self, offset, digits):
        """ Get the shortcode from the number """
        # Duplication of digits is not allowed.
        if len(digits) != len(set(digits)):
            raise Exception('Duplication in digits is not allowed.')

        self.offset = offset
        self.digits = digits


    def get_shortcode(self, number):
        """ Get the shortcode from the number """
        still_more = 1
        alpha = []
        nom = number + self.offset

        # Divide and conquer
        while still_more:
            still_more, moddy = divmod(nom, len(self.digits ))
            alpha.append(self.digits[moddy])
            nom = nom/len(self.digits)

        # Reverse, join, return
        alpha.reverse()
        return ''.join(alpha)


    def get_number(self, shortcode):
        """ Get the number from the shortcode. """
        if not shortcode:
            raise Error
        base = len(self.digits)
        number = self.digits.index(shortcode[0])
        if len(shortcode) > 1:
            for digit in shortcode[1:]:
                number = number * base
                number += self.digits.index(digit)
        number -= self.offset
        if number <= 0:
            return None
        return number


if __name__ == "__main__":
    import doctest
    doctest.testmod()
