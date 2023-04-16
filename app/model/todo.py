from graphene import ObjectType, String, Boolean, Field


class Todo(ObjectType):
    id = String()
    title = String()
    description = String()
    completed = Boolean()
