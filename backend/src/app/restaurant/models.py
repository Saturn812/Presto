from django.db import models

from .constants import MENU_ITEM_DISH_TYPE_CHOICES, MENU_ITEM_DISH_TYPE_OTHER


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Modifier(models.Model):
    """Modifier model"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=False, default='', blank=True)
    modifiers = models.ManyToManyField('self')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class MenuItem(models.Model):
    """Menu Item model"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=False, default='', blank=True)
    dish_type = models.CharField(max_length=31,
                                 choices=MENU_ITEM_DISH_TYPE_CHOICES,
                                 default=MENU_ITEM_DISH_TYPE_OTHER)
    modifiers = models.ManyToManyField(Modifier)
    restaurant = models.ForeignKey(Restaurant, null=False,
                                   on_delete=models.CASCADE)
