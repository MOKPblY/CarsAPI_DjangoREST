from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from myapi.models import Color, Model, Order, Vendor


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id','color')


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id','vendor')


class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Model
        fields = ('id','model','vendor')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'date', 'color', 'model', 'qty')



class OrderListSerializer(serializers.ModelSerializer):
    model = serializers.StringRelatedField(many=False)
    color = serializers.StringRelatedField(many=False)
    vendor = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'date', 'color', 'vendor', 'model', 'qty')#'vendor'

    def get_vendor(self, obj):
        return obj.model.vendor.vendor


class ColorStatsSerializer(serializers.Serializer):
    color = serializers.SerializerMethodField()
    total_qty = serializers.SerializerMethodField()

    def get_total_qty(self, obj):
        return obj['total_qty']

    def get_color(self, obj):
        return obj['color__color']


class VendorStatsSerializer(serializers.Serializer):
    vendor = serializers.SerializerMethodField()
    total_qty = serializers.SerializerMethodField()

    def get_vendor(self, obj):
        return obj['model__vendor__vendor']

    def get_total_qty(self, obj):
        return obj['total_qty']
