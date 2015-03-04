import unittest
import datetime
import decimal
import uuid
from rivr_rest_peewee.attributes import *


class TextAttributeTests(unittest.TestCase):
    def test_to_representation(self):
        attribute = TextAttribute()
        self.assertEqual(attribute.to_representation('value'), 'value')


class BooleanAttributeTests(unittest.TestCase):
    def test_to_representation(self):
        attribute = BooleanAttribute()
        representation = attribute.to_representation(True)
        self.assertEqual(representation, True)


class DateAttributeTests(unittest.TestCase):
    def test_to_representation(self):
        attribute = DateAttribute()
        value = datetime.date(year=2015, month=2, day=5)
        representation = attribute.to_representation(value)
        self.assertEqual(representation, '2015-02-05')


class DateTimeAttributeTests(unittest.TestCase):
    def test_to_representation(self):
        attribute = DateTimeAttribute()
        value = datetime.datetime(year=2015, month=2, day=5)
        representation = attribute.to_representation(value)
        self.assertEqual(representation, '2015-02-05T00:00:00')


class TimeAttributeTests(unittest.TestCase):
    def test_to_representation(self):
        attribute = TimeAttribute()
        value = datetime.time(hour=1, minute=30)
        representation = attribute.to_representation(value)
        self.assertEqual(representation, '01:30:00')


class IntegerAttributeTests(unittest.TestCase):
    def test_to_representation(self):
        attribute = IntegerAttribute()
        value = 5
        representation = attribute.to_representation(value)
        self.assertEqual(representation, 5)


class FloatAttributeTests(unittest.TestCase):
    def test_to_representation(self):
        attribute = FloatAttribute()
        value = 5
        representation = attribute.to_representation(value)
        self.assertEqual(representation, 5.0)


class DecimalAttributeTests(unittest.TestCase):
    def test_to_representation(self):
        attribute = DecimalAttribute()
        value = decimal.Decimal(5)
        representation = attribute.to_representation(value)
        self.assertEqual(representation, '5')


class UUIDAttributeTests(unittest.TestCase):
    def test_to_representation(self):
        attribute = UUIDAttribute()
        value = uuid.UUID('12345678123456781234567812345678')
        representation = attribute.to_representation(value)
        self.assertEqual(representation, '12345678-1234-5678-1234-567812345678')

