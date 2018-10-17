from rest_framework import mixins, permissions
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import Modifier, MenuItem, Restaurant
from .serializers import (MenuItemSerializer, RestaurantSerializer,
                          ModifierSerializer)


class RestaurantViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class MenuItemViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MenuItemSerializer
    queryset = MenuItem.objects.all()

    def get_queryset(self):
        return super(MenuItemViewSet, self).get_queryset().filter(
            restaurant_id=self.kwargs.get('restaurant_pk'))


class ModifierViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ModifierSerializer
    queryset = Modifier.objects.all()

    def get_queryset(self):
        return super(ModifierViewSet, self).get_queryset().filter(
            restaurant_id=self.kwargs.get('restaurant_pk'))


class MenuItemModifierViewSet(GenericViewSet, mixins.DestroyModelMixin):
    """Menu Item Modifier viewset

    Viewset to delete the menu item - modifier relationship
    """

    permission_classes = (permissions.AllowAny,)
    queryset = MenuItem.objects.all()

    def get_queryset(self):
        return super(MenuItemModifierViewSet, self).get_queryset().filter(
            id=self.kwargs.get('item_pk'),
            restaurant_id=self.kwargs.get(
                'restaurant_pk'))
