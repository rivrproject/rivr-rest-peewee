from rivr_rest import Resource

class PeeweeResource(Resource):
    model = None
    query = None
    lookup = 'id'

    slug_field = 'id'
    slug_uri_parameter = 'id'

    def __init__(self, parameters=None, obj=None):
        self.parameters = parameters
        self.obj = obj

    def get_parameters(self):
        return {
            self.slug_uri_parameter: getattr(self.get_object(), self.slug_field)
        }

    def get_query(self):
        if self.query:
            return self.query

        if self.model:
            return self.model.select()

    def get_object(self):
        if self.obj:
            return self.obj

        lookup = self.parameters[self.slug_uri_parameter]
        query = self.get_query().filter(**{self.slug_field: lookup})
        return query.get()


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
