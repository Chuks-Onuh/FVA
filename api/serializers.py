from .models import (
        Vendor, 
        Customer, 
        Menu, 
        Order, 
        Notification, 
        OrderStatus, 
        MessageStatus, 
        Cart, 
        BillingAddress, 
        AuthUser
)
from rest_framework import serializers



class AuthUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {'input_type': 'password'}, write_only = True)
    class Meta:
        model = AuthUser
        fields = ('pk',
                'email', 
                'password',
                'password2',
                'dateTimeCreated'
                )
        extra_kwargs = { 'password': {'write_only': True} }
        
    def save(self):
        user = AuthUser(
                email = self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match.'})
        user.set_password(password)
        user.save()
        return user
        
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
            'vendorId'
            'isRecurring', 
            'frequencyOfReocurence', 
        )


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = (
            'pk', 
            'customer',
            'vendorId',
            'description', 
            'itemsOrdered', 
            'dateAndTimeOfOrder', 
            'amountDue', 
            'amountPaid', 
            'amountOutstanding',  
            'orderStatus', 
            'menu', 
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
            'subjectUser',
            'order',
            'message', 
            'dateTimeCreated', 
            'messageStatus', 
        )


class MessageStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageStatus
        fields = (
            'pk', 
            'name', 
        )
        
class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = (
            'pk',
            'quantity',
            'dateTimeCreated',
            'itemsOrdered',     
        )

class BillingAddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BillingAddress
        fields = (
            'address',
            'zipcode',
            'city',
            'landmark',
            'name',
        )

