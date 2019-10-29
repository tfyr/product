from graphene_django import DjangoObjectType
from product.models import Item


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


