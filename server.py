from fastapi import FastAPI
from graphene import ObjectType, String, Field, Schema
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
import uvicorn

# Define GraphQL Schema


class Query(ObjectType):
    hello = String(description="A simple GraphQL query to return a greeting.")

    def resolve_hello(parent, info):
        return "Hello, GraphQL with FastAPI and Graphene!"


# Create FastAPI app
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Mount GraphQL endpoint
app.add_route("/graphql", GraphQLApp(schema=Schema(query=Query)))

app.add_route(
    "/graphiql",
    GraphQLApp(schema=Schema(query=Query),
               on_get=make_graphiql_handler())
)


# Start the FastAPI server
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
