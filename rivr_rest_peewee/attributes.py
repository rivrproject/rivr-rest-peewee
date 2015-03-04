import six


class Attribute(object):
    def to_representation(self, value):
        raise NotImplementedError('to_representation is not implemented.')


class TextAttribute(Attribute):
    def to_representation(self, value):
        return six.text_type(value)


class BooleanAttribute(Attribute):
    def to_representation(self, value):
        return value


class DateAttribute(Attribute):
    def to_representation(self, value):
        return value.isoformat()


class DateTimeAttribute(Attribute):
    def to_representation(self, value):
        return value.isoformat()


class TimeAttribute(Attribute):
    def to_representation(self, value):
        return value.isoformat()


class IntegerAttribute(Attribute):
    def to_representation(self, value):
        return int(value)


class FloatAttribute(Attribute):
    def to_representation(self, value):
        return float(value)


class DecimalAttribute(Attribute):
    def to_representation(self, value):
        return six.text_type(value)


class UUIDAttribute(Attribute):
    def to_representation(self, value):
        return six.text_type(value)

