import inspect
import peewee
from rivr_rest import Resource
from rivr_rest_peewee.attributes import *

class PeeweeResource(Resource):
    model = None
    query = None

    slug_field = 'id'
    slug_uri_parameter = 'id'

    field_attribute_map = {
        peewee.CharField: TextAttribute,
        peewee.TextField: TextAttribute,
        peewee.BooleanField: BooleanAttribute,
        peewee.DateTimeField: DateTimeAttribute,
        peewee.DateField: DateAttribute,
        peewee.TimeField: TimeAttribute,
        peewee.UUIDField: UUIDAttribute,
        peewee.IntegerField: IntegerAttribute,
        peewee.FloatField: FloatAttribute,
        peewee.DecimalField: DecimalAttribute,
    }

    def __init__(self, parameters=None, obj=None):
        self.parameters = parameters
        self.obj = obj

    # Parameters

    def get_parameters(self):
        return {
            self.slug_uri_parameter: getattr(self.get_object(), self.slug_field)
        }

    # Attributes

    def get_attribute_keys(self):
        """
        Returns all of the attribute keys to serialise into attributes. By
        default, this will introspect your model and use all non-foreign key
        field names.
        """

        fields = self.get_model()._meta.fields

        def key_filter(name):
            return name != 'id' and not isinstance(fields[name], peewee.ForeignKeyField)

        return filter(key_filter, fields.keys())

    def get_attributes(self):
        attributes = self.get_attribute_keys()
        obj = self.get_object()
        fields = self.get_model()._meta.fields

        def attribute(name):
            attribute = self.attribute_for_field(name, fields[name])
            representation = attribute.to_representation(getattr(obj, name))
            return (name, representation)

        return dict(map(attribute, attributes))

    # Relations

    def get_relation_keys(self):
        """
        Returns all of the relation keys to serialise into relations. By
        default, this will introspect your model and return all non-foreign key
        field names where there is a property on your resource for the related
        resource.
        """

        fields = self.get_model()._meta.fields
        is_relation = lambda name: isinstance(fields[name], peewee.ForeignKeyField)
        relations = filter(is_relation, fields.keys())
        reverse_relations = self.get_model()._meta.reverse_rel.keys()
        has_resource = lambda key: hasattr(self, key)
        return filter(has_resource, relations + reverse_relations)

    def get_relations(self):
        keys = self.get_relation_keys()
        obj = self.get_object()

        def relation(key):
            resource = getattr(self, key)
            value = getattr(obj, key)

            if isinstance(value, (list, tuple, peewee.SelectQuery)):
                return (key, map(lambda o: resource(obj=o), value))

            return (key, resource(obj=value))

        return dict(map(relation, keys))

    # Other

    def get_query(self):
        if self.query:
            return self.query

        if self.model:
            return self.model.select()

    def get_model(self):
        if self.model:
            return self.model

        if self.query:
            return self.query.model_class

    def get_object(self):
        if self.obj:
            return self.obj

        lookup = self.parameters[self.slug_uri_parameter]
        query = self.get_query().filter(**{self.slug_field: lookup})
        return query.get()

    # Private

    def attribute_for_field(self, field_name, field):
        """
        Returns an attribute for the given model field.
        """

        for klass in inspect.getmro(field.__class__):
            if klass in self.field_attribute_map:
                return self.field_attribute_map[klass]()

        raise KeyError('Attribute not found for {}'.format(field))


class PeeweeListResource(Resource):
    model = None
    query = None
    relation = 'objects'
    resource = PeeweeResource

    def get_query(self):
        if self.query:
            return self.query

        if self.model:
            return self.model.select()

    def get_objects(self):
        return self.get_query()

    def get_relations(self):
        return {
            self.relation: map(lambda obj: self.resource(obj=obj), self.get_objects())
        }
