from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import (
    RestaurantViewSet, MenuItemViewSet, ModifierViewSet,
    MenuItemModifierViewSet)

router = DefaultRouter()
router.register('', RestaurantViewSet, base_name='restaurants')
router.register(r'(?P<restaurant_pk>\w+)/items', MenuItemViewSet,
                base_name='menu-items')
router.register(r'(?P<restaurant_pk>\w+)/items/(?P<item_pk>\w+)',
                MenuItemModifierViewSet, base_name='menu-item-modifiers')
router.register(r'(?P<restaurant_pk>\w+)/modifiers', ModifierViewSet,
                base_name='modifiers')

restaurant_urlpatterns = [
    url(r'^', include(router.urls)),
]
