
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from myapi.models import Order
from myapi.views import ColorViewSet, VendorViewSet, ModelViewSet, OrderViewSet, ColorStatsViewSet, VendorStatsViewSet
from test1 import settings

color_router = routers.SimpleRouter()
vendor_router = routers.SimpleRouter()
model_router = routers.SimpleRouter()
order_router = routers.SimpleRouter()
colorstats_router = routers.SimpleRouter()
vendorstats_router = routers.SimpleRouter()

color_router.register(r'colors', ColorViewSet)
vendor_router.register(r'vendors', VendorViewSet)
model_router.register(r'models', ModelViewSet)
order_router.register(r'orders', OrderViewSet, basename=Order)
colorstats_router.register(r'colorstats', ColorStatsViewSet)
vendorstats_router.register(r'vendorstats', VendorStatsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(color_router.urls)),
    path('api/', include(vendor_router.urls)),
    path('api/', include(model_router.urls)),
    path('api/', include(order_router.urls)),
    path('api/', include(colorstats_router.urls)),
    path('api/', include(vendorstats_router.urls))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]