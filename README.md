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
```

Create a simple resource from a peewee model:

```python
class UserResource(PeeweeResource):
    model = User
    url_template = '/users/{id}'

    def get_attributes(self):
        user = self.get_object()

        return {
            'user': user.name,
        }
```

Show a list of model resources:

```python
class UserListResource(PeeweeListResource):
    model = User
    uri_template = '/users'
    relation = 'users'
    resource = UserResource
```

## License

rivr-rest-peewee is released under the BSD license. See [LICENSE](LICENSE).

