from .models import Vendor, Customer, Menu, Order, OrderStatus, Notification, MessageStatus, Cart, BillingAddress
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    CustomerSerializer, 
    MenuSerializer, 
    MessageStatusSerializer, 
    NotificationSerializer,
    OrderSerializer,
    OrderStatusSerializer,
    VendorSerializer, 
    CartSerializer, 
    BillingAddressSerializer,
    AuthUserSerializer
)


@api_view(['POST'])
def authuser_view(request):
    if request.Method == 'POST':
        serializer = AuthUserSerializer(date = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Successfully registered.'
            data['email'] = account.email
        else:
            data = serializer.errors
        return Response(data)
        
        
class VendorListView(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorCreateView(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    

class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()   
    serializer_class = OrderSerializer


class OrderRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderStatusListView(generics.ListAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

class OrderStatusCreateView(generics.CreateAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

class OrderStatusRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

class NotificationListView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationCreateView(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class NotificationRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class =NotificationSerializer

class MessageStatusListView(generics.ListAPIView):
    queryset = MessageStatus.objects.all()
    serializer_class = MessageStatusSerializer


class MessageStatusCreateView(generics.CreateAPIView):
    queryset = MessageStatus.objects.all()
    serializer_class = MessageStatusSerializer


class MessageStatusRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MessageStatus.objects.all()
    serializer_class = MessageStatusSerializer
    
class CartListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class CartRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class BillingAddressListView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
class BillingAddressCreateView(generics.CreateAPIView):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer
    
class BillingAddressRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillingAddress.objects.all()
    serializer_class = BillingAddressSerializer

