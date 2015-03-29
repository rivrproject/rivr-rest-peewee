# rivr-rest-peewee

[![Build Status](http://img.shields.io/travis/rivrproject/rivr-rest-peewee/master.svg?style=flat)](https://travis-ci.org/rivrproject/rivr-rest-peewee)

Library for building REST APIs with rivr and peewee. Extends [rivr-rest](https://github.com/rivrproject/rivr-rest) to aid building resources from Peewee models.

## Installation

```bash
$ pip install rivr-rest-peewee
```

## Usage

```python
from rivr_rest_peewee import PeeweeResource, PeeweeListResource

class Task(Model):
    text = peewee.CharField()
```

Create a simple resource from a peewee model:

```python
class TaskResource(PeeweeResource):
    model = Task
    url_template = '/tasks/{id}'
```

#### Attributes

`PeeweeResource` automatically serialises the attributes of your model. You can alter the fields used by implementing `get_attribute_keys()` on your resource as follows:

```python
def get_attribute_keys(self):
    return ('text',)
```

Of course, if you don’t want automatic serialisation, you may create your own implementation of `get_attributes()` on your resource.

#### Relations

`PeeweeResource` can automatically build relations to other models from foreign key or to-many relations, providing you supply it with a resource for that model:

```python
# Models
class User(Model):
    pass

class Task(Model):
    text = peewee.CharField()
    creator = peewee.ForeignKeyField(User)

# Resources
class UserResource(PeeweeResource):
    model = User
    url_template = '/users/{id}'

class TaskResource(PeeweeResource):
    model = Task
    url_template = '/tasks/{id}'

    creator = UserResource
```

Again, you can alter the fields used by implementing `get_relation_keys()`:

```python
def get_relation_keys(self):
    return ('creator',)
```

### Collection of peewee resources

```python
class TaskListResource(PeeweeListResource):
    model = Task
    uri_template = '/tasks'
    relation = 'tasks'
    resource = TaskResource
```

## License

rivr-rest-peewee is released under the BSD license. See [LICENSE](LICENSE).

