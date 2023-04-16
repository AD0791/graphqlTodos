from graphene import Field, List, ObjectType, Schema, String

from ..service import CreateTodoMutation
from ..model import Todo


class Query(ObjectType):
    todo = Field(lambda: Todo, id=String())
    todos = Field(lambda: List(Todo))

    def resolve_todo(self, root, info, id):
        return next((todo for todo in todos if todo.id == id), None)
        return todo

    def resolve_todos(self, info):
        return todos


class Mutation(ObjectType):
    create_todo = CreateTodoMutation.Field()


todoSchema = Schema(query=Query, mutation=Mutation,)
