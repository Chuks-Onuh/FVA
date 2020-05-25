from django.contrib import admin
from django import forms
from .models import (
    Vendor, 
    Customer, 
    Menu, 
    Order, 
    OrderStatus, 
    Notification, 
    MessageStatus, 
    Cart, 
    BillingAddress, 
    AuthUser   
)

class AuthAdminForm(forms.ModelForm):
    
    class Meta:
        model = AuthUser
        fields = '__all__'
        
class AuthUserAdmin(admin.ModelAdmin):
    form = AuthAdminForm
    list_display = ['email', 'password', 'dateTimeCreated']
    
admin.site.register(AuthUser, AuthUserAdmin)

class VendorAdminForm(forms.ModelForm):

    class Meta:
        model = Vendor
        fields = '__all__'


class VendorAdmin(admin.ModelAdmin):
    form = VendorAdminForm
    list_display = ['businessname', 'email', 'phoneNumber', 'dateTimeCreated']

admin.site.register(Vendor, VendorAdmin)


class CustomerAdminForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class CustomerAdmin(admin.ModelAdmin):
    form = CustomerAdminForm
    list_display = ['firstname', 'lastname', 'email', 'phoneNumber', 'dateTimeCreated', 'amountOutstanding']
    
    
admin.site.register(Customer, CustomerAdmin)


class MenuAdminForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = '__all__'


class MenuAdmin(admin.ModelAdmin):
    form = MenuAdminForm
    list_display = ['name', 'description', 'price', 'quantity', 'dateTimeCreated', 'vendorId',
                    'isRecurring', 'frequencyOfReocurence',]

admin.site.register(Menu, MenuAdmin)


class OrderAdminForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class OrderAdmin(admin.ModelAdmin):
    form = OrderAdminForm
    list_display = ['description', 'itemsOrdered', 'dateAndTimeOfOrder', 'amountDue', 
                'amountPaid', 'amountOutstanding', 'vendorId', 'orderStatus', 'menuId']

admin.site.register(Order, OrderAdmin)


class OrderStatusAdminForm(forms.ModelForm):

    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderStatusAdmin(admin.ModelAdmin):
    form = OrderStatusAdminForm
    list_display = ['name']

admin.site.register(OrderStatus, OrderStatusAdmin)


class NotificationAdminForm(forms.ModelForm):

    class Meta:
        model = Notification
        fields = '__all__'


class NotificationAdmin(admin.ModelAdmin):
    form = NotificationAdminForm
    list_display = ['subjectUser','order', 'message', 'dateTimeCreated' ,  'messageStatus']
    

admin.site.register(Notification, NotificationAdmin)


class MessageStatusAdminForm(forms.ModelForm):

    class Meta:
        model = MessageStatus
        fields = '__all__'


class MessageStatusAdmin(admin.ModelAdmin):
    form = MessageStatusAdminForm
    list_display = ['name']
    readonly_fields = ['name']

admin.site.register(MessageStatus, MessageStatusAdmin)


class CartAdminForm(forms.ModelForm):
    
    class Meta:
        model = Cart
        fields = '__all__'
        
class CartAdmin(admin.ModelAdmin):
    
    form = CartAdminForm
    list_dispaly = ['itemsOrdered', 'quantity', 'dateTimeCreated']
    
admin.site.register(Cart, CartAdmin)


class BillingAddressAdminForm(forms.ModelForm):
    
    class Meta:
        model = BillingAddress
        fields = '__all__'
        
class BillingAddressAdmin(admin.ModelAdmin):
    
    form = BillingAddressAdminForm
    list_dispaly = ['address', 'zipcode', 'city', 'landmark', 'name']
    
admin.site.register(BillingAddress, BillingAddressAdmin)


