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


class CreateCategoryInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String(required=False)


class CreateCategory(graphene.Mutation):
    class Arguments:
        category_data = CreateCategoryInput(required=True)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    def mutate(self, info, category_data=None):

        #category = CategoryType(name=name,description="aa")
        ok=True
        obj = Category.objects.create(name=category_data.name,description=category_data.description)
        return CreateCategory(category=obj,ok=ok)


class UpdateCategoryInput(graphene.InputObjectType):
    name = graphene.String(required=False)
    description = graphene.String(required=False)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        category_id=graphene.Int(required=True)
        category_data = UpdateCategoryInput(required=False)

    ok = graphene.Boolean()
    category = graphene.Field(CategoryType)

    def mutate(self, info, category_id,category_data=None):

        old_object =  Category.objects.get(id=category_id)
        updated_values = {'name': old_object.name, 'description': old_object.description}

        if category_data is not None:
            if category_data.name is not None:
                updated_values['name'] = category_data.name
            if category_data.description is not None:
                updated_values['description'] = category_data.description

        obj,created = Category.objects.update_or_create(id=category_id,defaults=updated_values)
        ok = True
        return UpdateCategory(category=obj,ok=ok)


class DeleteCategory(graphene.Mutation):
    class Arguments:
        category_id=graphene.Int(required=True)

    deleted = graphene.Boolean()
    category_deleted_id = graphene.Int()

    def mutate(self, info, category_id):

        Category.objects.filter(id=category_id).delete()
        deleted = True

        return DeleteCategory(deleted=deleted,category_deleted_id=category_id)


class CreateDishInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    category_id = graphene.Int(required=True)
    description = graphene.String(required=False)
    price = graphene.Int(required=False)


class CreateDish(graphene.Mutation):
    class Arguments:
        create_dish_input= CreateDishInput(required=False)

    ok = graphene.Boolean()
    dish = graphene.Field(DishType)

    def mutate(self,info,create_dish_input):

        obj = Dish.objects.create(name=create_dish_input.name,
                                  category_id=create_dish_input.category_id,
                                  description=create_dish_input.description,
                                  price=create_dish_input.price)
        ok = True
        return CreateDish(dish = obj,ok = ok)


class UpdateDishInput(graphene.InputObjectType):
    name = graphene.String(required=False)
    description = graphene.String(required=False)
    price = graphene.Int(required=False)


class UpdateDish(graphene.Mutation):
    class Arguments:
        dish_id = graphene.Int(required=True)
        dish_data = UpdateDishInput(required=False)

    ok = graphene.Boolean()
    dish = graphene.Field(DishType)

    def mutate(self,info,dish_id,dish_data=None):

        old_object = Dish.objects.get(id=dish_id)
        updated_values = {'name': old_object.name, 'description': old_object.description,'price':old_object.price}

        if dish_data is not None:
            if dish_data.name is not None:
                updated_values['name'] = dish_data.name
            if dish_data.description is not None:
                updated_values['description'] = dish_data.description
            if dish_data.price is not None:
                updated_values['price'] = dish_data.price

        obj,created = Dish.objects.update_or_create(id=dish_id,defaults=updated_values)
        ok = True
        return UpdateDish(dish=obj, ok=ok)


class DeleteDish(graphene.Mutation):
    class Arguments:
        dish_id = graphene.Int(required=True)

    deleted = graphene.Boolean()
    dish_deleted_id = graphene.Int()

    def mutate(self,info,dish_id):
        Dish.objects.filter(id=dish_id).delete()
        deleted = True

        return DeleteDish(deleted=deleted,dish_deleted_id=dish_id)


class Mutation(graphene.AbstractType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()
    delete_category = DeleteCategory.Field()

    create_dish = CreateDish.Field()
    update_dish = UpdateDish.Field()
    delete_dish = DeleteDish.Field()







