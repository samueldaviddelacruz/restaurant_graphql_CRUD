import graphene

import restaurantapi.schema



class Query(restaurantapi.schema.Query,graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutations(restaurantapi.schema.Mutation,graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass






schema = graphene.Schema(query=Query,mutation=Mutations)