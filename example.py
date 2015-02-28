from rivr import serve
from rivr_peewee import Database
from rivr_rest import Router
from rivr_rest_peewee import PeeweeResource, PeeweeListResource
import peewee


"""
A simple Todo API using rivr-rest-peewee.
"""

## Models:

database = Database(peewee.SqliteDatabase('example.sqlite'))

class Task(database.Model):
    text = peewee.CharField()

    def __str__(self):
        return self.text


## Resources

class TaskResource(PeeweeResource):
    model = Task
    uri_template = '/tasks/{id}'

    def get_attributes(self):
        return { 'text': self.get_object().text }


class TaskListResource(PeeweeListResource):
    uri_template = '/tasks'
    model = Task
    relation = 'tasks'
    resource = TaskResource


router = Router(
    TaskListResource,
    TaskResource,
)

router.add_root_resource('tasks', TaskListResource)

if __name__ == '__main__':
    try:
        Task.create_table()
        Task.create(text='My first task')
    except:
        # Database is already created
        pass

    serve(database(router))

