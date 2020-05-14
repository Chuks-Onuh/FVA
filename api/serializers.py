from .models import Vendor, Customer, Menu, Order, Notification, OrderStatus, MessageStatus

from rest_framework import serializers


class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = (
            'pk', 
            'businessname', 
            'email', 
            'phoneNumber', 
            'dateTimeCreated', 
        )


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            'pk', 
            'firstname', 
            'lastname', 
            'email', 
            'phoneNumber', 
            'dateTimeCreated', 
            'amountOutstanding', 
        )


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = (
            'pk', 
            'name', 
            'description', 
            'price', 
            'quantity', 
            'dateTimeCreated', 
            'isRecurring', 
            'frequencyOfReocurence', 
            'vendorId'
        )


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'pk', 
            'description', 
            'itemsOrdered', 
            'dateAndTimeOfOrder', 
            'amountDue', 
            'amountPaid', 
            'amountOutstanding', 
            'vendorId', 
            'orderStatus', 
            'menuId', 
        )


class OrderStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderStatus
        fields = (
            'pk', 
            'name', 
        )


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = (
            'pk', 
            'message', 
            'dateTimeCreated', 
            'subjectUser', 
            'messageStatus', 
            'orderId'
        )


class MessageStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageStatus
        fields = (
            'pk', 
            'name', 
        )


