# rivr-rest-peewee

[![Build Status](http://img.shields.io/travis/rivrproject/rivr-rest-peewee/master.svg?style=flat)](https://travis-ci.org/rivrproject/rivr-rest-peewee)

Library for building REST APIs with rivr and peewee.

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

`PeeweeResource` automatically serialise the attributes of your model. You can alter the fields to use by implementing `get_attribute_keys()` on your resource as follows:

```python
def get_attributes(self):
    return ('text',)
```

Of course, if you don’t want automatic serialisation, you may create your own implementation of `get_attributes()` on your resource.

Show a list of model resources:

```python
class TaskListResource(PeeweeListResource):
    model = Task
    uri_template = '/tasks'
    relation = 'tasks'
    resource = TaskResource
```

## License

rivr-rest-peewee is released under the BSD license. See [LICENSE](LICENSE).

