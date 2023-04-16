from graphene import Mutation, String, Field
from ..model import Todo
from uuid import uuid4


class CreateTodoMutation(Mutation):
    class Arguments:
        title = String(required=True)
        description = String(required=True)

    todo = Field(lambda: Todo)

    def mutate(self, info, title, description):
        # Create a new todo
        todo = Todo(
            id=uuid4(),  # You can generate an id using your preferred method
            title=title,
            description=description,
            completed=False
        )
        # Save the todo to your data store or database
        # Add the logic to save the todo to your data store or database here
        # ...

        return CreateTodoMutation(todo=todo)
