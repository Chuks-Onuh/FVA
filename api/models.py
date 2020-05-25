from django.urls import reverse
#from django_extensions.db.fields import AutoSlugField
from django.contrib.postgres.fields import ArrayField
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import IntegerField
from django.db.models import TextField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models
from django_extensions.db import fields as extension_fields
from django.shortcuts import get_object_or_404
from django.contrib import messages
from phone_field import PhoneField
import jsonfield
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class AuthUser(AbstractUser):
    
    # Fields
    username =  None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    dateTimeCreated = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()
    def __str__(self):
        return self.email
    
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})


class Vendor(models.Model):
    
    # Fields
    businessname = models.CharField(max_length=100)
    email = models.EmailField(unique = True, blank = False)
    phoneNumber = PhoneField(blank=True, help_text='Contact phone number')
    dateTimeCreated = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('api_vendor_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('api_vendor_update', args=(self.pk,))
    
    def __str__(self):
        return self.businessname


class Customer(models.Model):

    # Fields
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique = True, blank = False)
    phoneNumber = PhoneField(blank=True, help_text='Contact phone number')
    dateTimeCreated = models.DateTimeField(auto_now_add=True)
    amountOutstanding = models.FloatField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    
    
    def __str__(self):
        return self.firstname +  self. lastname


class Menu(models.Model):

    # Fields
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True) 
    price = models.FloatField()
    quantity = models.IntegerField()
    dateTimeCreated = models.DateTimeField(auto_now_add=True, editable=True)
    # Relationship Fields
    vendorId = models.ForeignKey(
        'api.Vendor',
        on_delete=models.CASCADE
    )
    isRecurring = models.BooleanField()
    frequencyOfReocurence = models.CharField(max_length=30)

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        """Returns the url to access a detailed menu"""
        return reverse('api_menu_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('api_menu_update', args=(self.pk,))


class Order(models.Model):

    STATUS_CHOICES = (
    (1, 'Pendind'),
    (2, 'Delivered'),
    (3, 'Cancelled'),
    )
    # Fields
    
    # Relationship Fields
    customerId = models.ForeignKey(
        'api.Customer',
        on_delete=models.CASCADE 
    )
    vendorId = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE
    )
    description = models.TextField(max_length=100)
    itemsOrdered = ArrayField(
    ArrayField(
        models.CharField(max_length=10, blank=True)
    ),
    size=1
)
    itemsOrdered = ArrayField(models.CharField(max_length=50), blank=True)
    amountDue = models.FloatField()
    amountPaid = models.FloatField()
    amountOutstanding = models.FloatField()
    orderStatus = models.IntegerField(choices=STATUS_CHOICES)
    # Relationship Field
    menuId = models.ForeignKey(
        'api.Menu',
        on_delete=models.CASCADE
    )
    dateAndTimeOfOrder = models.DateTimeField(auto_now_add=True, editable=True)
    
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        """Returns the url to access a detailed order"""
        return reverse('api_order_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('api_order_update', args=(self.pk,))
    
    # get total itemsOrdered
    
    def get_total(self):
        total = self.amountDue + self.amountPaid + self.amountOutstanding
        amountOutstanding = self.amountDue - self.amountPaid
        if total:
            return 'Total amount for your purchased items is  {}'.format(amountDue)
        else:
            return 'Your amount outstanding is {}'.format(amountOutstanding)
    


class OrderStatus(models.Model):

    # Fields
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        """Returns the url to access a detailed order_status"""
        return reverse('api_orderstatus_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('api_orderstatus_update', args=(self.pk,))


class Notification(models.Model):

    # Fields
    
    # Relationship Fields
    subjectUser = models.ForeignKey(
        Vendor,
        on_delete = models.CASCADE
    )
    orderId = models.ForeignKey(
        'api.Order',
        on_delete=models.CASCADE
    )
    message = models.TextField()
    dateTimeCreated = models.DateTimeField(auto_now_add=True, editable=True)
    # Relationship Field
    messageStatus = models.ForeignKey(
        'api.MessageStatus',
        on_delete=models.CASCADE
    )
    
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        """Returns the url to access a detailed notification"""
        return reverse('api_notification_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('api_notification_update', args=(self.pk,))


class MessageStatus(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        """Returns the url to access a detailed message_status"""
        return reverse('api_messagestatus_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('api_messagestatus_update', args=(self.pk,))
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):  
    # Fields
    quantity = models.IntegerField(default=1)
    dateTimeCreated = models.DateTimeField(auto_now_add=True)
        
    # Relationship Fields
    itemsOrdered = models.ManyToManyField(
        Order
        )
    def __str__(self):
        return f'{self.quantity} of {self.itemsOrdered.name}'
        
    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        """Returns the url to access a detailed cart"""
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('api_cart_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('api_cart_update', args=(self.pk,))
    
    # Getting the total price of items in the cart
    
    def get_total(self):
        total = itemsOrdered.amountDue * self.quantity
        float_total = float('{0:.2f}'.format(total))
        return float_total
        return 'paid'

class BillingAddress(models.Model):
    # Fields
    
    # Relationship Fields
    name = models.ForeignKey('api.Customer',
    on_delete=models.CASCADE
    )
    itemsOrdered = models.ManyToManyField(
    Order
    )
    
    address = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 50)
    city = models.CharField(max_length = 30)
    landmark = models.CharField(max_length = 50)
    
    
    class Meta:
        verbose_name_plural = "Shipping Addresses"

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        """Returns the url to access a detailed billing address"""
        return reverse('api_billingaddress_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('api_billingaddress_update', args=(self.pk,))