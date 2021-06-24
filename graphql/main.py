# https://testdriven.io/blog/fastapi-graphql/
# https://github.com/graphql-python/graphene-pydantic
# https://dgraph.io/docs/clients/python/

from fastapi import FastAPI
import graphene
from starlette.graphql import GraphQLApp

from schema import Query, Mutation

app = FastAPI()

app.add_route('/graphql', GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))

@app.get('/')
def ping():
    return {"ping": "pong"}