from django.conf.urls import url, include

from app.restaurant.urls import restaurant_urlpatterns

urlpatterns = [
    url(r'^restaurant/', include(restaurant_urlpatterns)),
]
