import django_filters
from django.db.models import Sum, Count
from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, mixins, filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from myapi.models import Color, Model, Order, Vendor
from myapi.serializers import ColorSerializer, ModelSerializer, VendorSerializer, OrderSerializer, ColorStatsSerializer, \
    VendorStatsSerializer, OrderListSerializer


class OrderListViewSetPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 10
    page_size_query_param = 'page_size'


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects
    serializer_class = ColorSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects
    serializer_class = VendorSerializer

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects
    serializer_class = ModelSerializer

class OrderViewSet(viewsets.ModelViewSet):
    pagination_class = OrderListViewSetPagination
    queryset = Order.objects.select_related('color', 'model', 'model__vendor').all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['model__vendor']
    ordering_fields = ['qty']


    def get_serializer_class(self):
        if self.action == 'list':
            return OrderListSerializer
        else:
            return OrderSerializer

    # def get_queryset(self):
    #     if self.action == 'list':
    #         return Order.objects.select_related('color', 'model', 'model__vendor').all()
    #     else:
    #         return Order.objects.all()


class ColorStatsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Order.objects.select_related('color').values('color__color').annotate(total_qty = Sum('qty'))
    serializer_class = ColorStatsSerializer


class VendorStatsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Order.objects.select_related('model__vendor').values('model__vendor__vendor').annotate(total_qty = Sum('qty'))
    serializer_class = VendorStatsSerializer

