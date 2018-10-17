from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .constants import MENU_ITEM_DISH_TYPE_CHOICES, MENU_ITEM_DISH_TYPE_OTHER
from .models import MenuItem, Restaurant, Modifier


class ModifierSerializer(serializers.ModelSerializer):
    """Modifier model serializer"""

    id = serializers.IntegerField(read_only=True)
    label = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True,
                                        default='')
    modifiers = serializers.ListField(child=RecursiveField(), required=False)

    class Meta:
        model = Modifier
        read_only_fields = ('id',)
        fields = ('id', 'label', 'description', 'modifiers',)


class MenuItemSerializer(serializers.ModelSerializer):
    """Menu Item model serializer"""

    id = serializers.IntegerField(read_only=True)
    label = serializers.CharField(required=True, max_length=255)
    description = serializers.CharField(required=False, allow_blank=True,
                                        default='')
    dish_type = serializers.ChoiceField(choices=MENU_ITEM_DISH_TYPE_CHOICES,
                                        default=MENU_ITEM_DISH_TYPE_OTHER)
    modifiers = ModifierSerializer(many=True, required=False)

    class Meta:
        model = MenuItem
        read_only_fields = ('id',)
        fields = ('id', 'label', 'description', 'dish_type', 'modifiers',)


class RestaurantSerializer(serializers.ModelSerializer):
    """Restaurant model serializer"""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    class Meta:
        model = Restaurant
        read_only_fields = ('id',)
        fields = ('id', 'name',)
