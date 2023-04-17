import graphene
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
import uvicorn


from app.schemas import todoSchema
# Create FastAPI app
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Mount GraphQL endpoint
app.add_route("/graphql", GraphQLApp(schema=todoSchema))

app.add_route(
    "/graphiql",
    GraphQLApp(schema=todoSchema,
               on_get=make_graphiql_handler())
)


""" # Start the FastAPI server
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000) """
