from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
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
from django.db import models as models
from django_extensions.db import fields as extension_fields
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField




class Vendor(models.Model):

    # Fields
    businessname = models.CharField(max_length=255)
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
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(unique = True, blank = False)
    phoneNumber = PhoneField(blank=True, help_text='Contact phone number')
    dateTimeCreated = models.DateTimeField(auto_now_add=True)
    amountOutstanding = models.IntegerField()


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('api_customer_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('api_customer_update', args=(self.pk,))
    
    
    def __str__(self):
        return self.firstname +  self. lastname


class Menu(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True) 
    price = models.IntegerField()
    quantity = models.IntegerField()
    dateTimeCreated = models.DateTimeField(auto_now_add=True, editable=True)
    isRecurring = models.BooleanField()
    frequencyOfReocurence = models.CharField(max_length=30)

     # Relationship Fields
    vendorId = models.ForeignKey(
        'api.Vendor',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('api_menu_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('api_menu_update', args=(self.pk,))
    
    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICES = (
    (1, 'Pendind'),
    (2, 'Delivered'),
    (3, 'Cancelled'),
    )

    # Fields
    description = models.TextField(max_length=255)
    itemsOrdered = ArrayField(models.CharField(max_length=50), blank=True)
    dateAndTimeOfOrder = models.DateTimeField(auto_now_add=True, editable=True)
    amountDue = models.IntegerField()
    amountPaid = models.IntegerField()
    amountOutstanding = models.IntegerField()
    orderStatus = models.IntegerField(choices=STATUS_CHOICES)

    # Relationship Fields
    customerId = models.ForeignKey(
        'api.Customer',
        on_delete=models.CASCADE 
    )
    vendorId = models.ForeignKey(
        'api.Vendor',
        on_delete=models.CASCADE
    )
    menuId = models.ForeignKey(
        'api.Menu',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('api_order_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('api_order_update', args=(self.pk,))


class OrderStatus(models.Model):

    # Fields
    name = models.CharField(max_length=255)


    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('api_orderstatus_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('api_orderstatus_update', args=(self.pk,))


class Notification(models.Model):

    # Fields
    message = models.TextField()
    dateTimeCreated = models.DateTimeField(auto_now_add=True, editable=True)
    
    # Relationship Fields
    orderId = models.ForeignKey(
        'api.Order',
        on_delete=models.CASCADE
    )
    subjectUser = models.ForeignKey(
        'api.Vendor',
        on_delete = models.CASCADE
    )
    messageStatus = models.ForeignKey(
        'api.MessageStatus',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-pk',)

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
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
        return reverse('api_messagestatus_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('api_messagestatus_update', args=(self.pk,))
    
    def __str__(self):
        return self.name


