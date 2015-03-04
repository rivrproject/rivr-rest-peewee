import unittest
import peewee
from rivr_rest_peewee.resources import PeeweeResource
from rivr_rest_peewee.attributes import *


class PeeweeResourceTests(unittest.TestCase):
    def setUp(self):
        self.resource = PeeweeResource()

    def check_attribute_type_for_field(self, field, attribute_type):
        attribute = self.resource.attribute_for_field('name', field)
        self.assertIsInstance(attribute, attribute_type)

    def test_attribute_for_char_field(self):
        self.check_attribute_type_for_field(peewee.CharField(), TextAttribute)

    def test_attribute_for_text_field(self):
        self.check_attribute_type_for_field(peewee.TextField(), TextAttribute)

    def test_attribute_for_boolean_field(self):
        self.check_attribute_type_for_field(peewee.BooleanField(), BooleanAttribute)

    def test_attribute_for_integer_field(self):
        self.check_attribute_type_for_field(peewee.IntegerField(), IntegerAttribute)

    def test_attribute_for_big_integer_field(self):
        self.check_attribute_type_for_field(peewee.BigIntegerField(), IntegerAttribute)

    def test_attribute_for_float_field(self):
        self.check_attribute_type_for_field(peewee.FloatField(), FloatAttribute)

    def test_attribute_for_double_field(self):
        self.check_attribute_type_for_field(peewee.DoubleField(), FloatAttribute)

    def test_attribute_for_decimal_field(self):
        self.check_attribute_type_for_field(peewee.DecimalField(), DecimalAttribute)

    def test_attribute_for_date_field(self):
        self.check_attribute_type_for_field(peewee.DateField(), DateAttribute)

    def test_attribute_for_date_time_field(self):
        self.check_attribute_type_for_field(peewee.DateTimeField(), DateTimeAttribute)

    def test_attribute_for_time_field(self):
        self.check_attribute_type_for_field(peewee.TimeField(), TimeAttribute)

    def test_attribute_for_uuid_field(self):
        self.check_attribute_type_for_field(peewee.UUIDField(), UUIDAttribute)
