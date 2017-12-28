import graphene
from graphene_django.types import DjangoObjectType
from restaurantapi.models import Category,Dish


class CategoryType(DjangoObjectType):

    class Meta:
        model = Category


class DishType(DjangoObjectType):

    class Meta:
        model = Dish


class Query(object):
    category = graphene.Field(CategoryType,
                                id=graphene.Int(),
                                name=graphene.String())

    all_categories = graphene.List(CategoryType)

    dish = graphene.Field(DishType,
                                id=graphene.Int(),
                                name=graphene.String())

    all_dishes = graphene.List(DishType)

    all_dishes_by_category = graphene.List(DishType,category_id=graphene.Int())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_dishes(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Dish.objects.select_related('category').all()


    def resolve_all_dishes_by_category(self, info, **kwargs):
        id = kwargs.get('category_id')

        if id is not None:
            return Dish.objects.select_related('category').filter(category=id)

        return None

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None

    def resolve_dish(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Dish.objects.get(pk=id)

        if name is not None:
            return Dish.objects.get(name=name)

        return None


class CreateCategory(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=False)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    def mutate(self, info, name,description):

        #category = CategoryType(name=name,description="aa")
        ok=True
        obj = Category.objects.create(name=name,description=description)
        return CreateCategory(category=obj,ok=ok)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        categoryId=graphene.Int(required=True)
        name = graphene.String(required=True)
        description = graphene.String(required=False)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    def mutate(self, info, categoryId,name, description):

        updated_values = {'name': name, 'description': description}
        ok = True
        obj,created = Category.objects.update_or_create(id=categoryId,defaults=updated_values)


        return CreateCategory(category=obj, ok=ok)


class Mutation(graphene.AbstractType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()





