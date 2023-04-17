from graphene import Field, List, ObjectType, Schema, String
from uuid import uuid4

from ..service import CreateTodoMutation
from ..model import Todo


class Query(ObjectType):
    todos = Field(lambda: List(Todo))

    def resolve_todos(self, info):
        todos = [
            Todo(id=uuid4(), title="Todo 1",
                 description="This is todo 1", completed=True),
            Todo(id=uuid4(), title="Todo 2",
                 description="This is todo 2", completed=False),
            Todo(id=uuid4(), title="Todo 3",
                 description="This is todo 3", completed=True),
        ]
        return todos


class Mutation(ObjectType):
    create_todo = CreateTodoMutation.Field()


todoSchema = Schema(query=Query, mutation=Mutation,)
