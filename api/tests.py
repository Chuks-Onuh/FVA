import unittest
from django.urls import reverse
from django.test import Client
from .models import Vendor, Customer, Menu, Order, OrderStatus, Notification, MessageStatus
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_vendor(**kwargs):
    defaults = {}
    defaults["businessname"] = "businessname"
    defaults["email"] = "email"
    defaults["phoneNumber"] = "phoneNumber"
    defaults.update(**kwargs)
    return Vendor.objects.create(**defaults)


def create_customer(**kwargs):
    defaults = {}
    defaults["firstname"] = "firstname"
    defaults["lastname"] = "lastname"
    defaults["email"] = "email"
    defaults["phoneNumber"] = "phoneNumber"
    defaults["amountOutstanding"] = "amountOutstanding"
    defaults.update(**kwargs)
    return Customer.objects.create(**defaults)


def create_menu(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["price"] = "price"
    defaults["quantity"] = "quantity"
    defaults["isRecurring"] = "isRecurring"
    defaults["frequencyOfReocurence"] = "frequencyOfReocurence"
    defaults.update(**kwargs)
    if "vendorId" not in defaults:
        defaults["vendorId"] = create_vendor()
    return Menu.objects.create(**defaults)


def create_order(**kwargs):
    defaults = {}
    defaults["description"] = "description"
    defaults["itemsOrdered"] = "itemsOrdered"
    defaults["amountDue"] = "amountDue"
    defaults["amountPaid"] = "amountPaid"
    defaults["amountOutstanding"] = "amountOutstanding"
    defaults["vendorId"] = "vendorId"
    defaults["orderStatus"] = "orderStatus"
    defaults["menuId"] = "menuId"
    defaults.update(**kwargs)
    if "customer" not in defaults:
        defaults["customer"] = create_customer()
    return Order.objects.create(**defaults)


def create_orderstatus(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return OrderStatus.objects.create(**defaults)


def create_notification(**kwargs):
    defaults = {}
    defaults["message"] = "message"
    defaults["subjectUserId"] = "subjectUserId"
    defaults["messageStatus"] = "messageStatus"
    defaults.update(**kwargs)
    if "order" not in defaults:
        defaults["order"] = create_order()
    return Notification.objects.create(**defaults)


def create_messagestatus(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return MessageStatus.objects.create(**defaults)


class VendorViewTest(unittest.TestCase):
    '''
    Tests for Vendor
    '''
    def setUp(self):
        self.client = Client()

    def test_list_vendor(self):
        url = reverse('fva_vendor_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_vendor(self):
        url = reverse('fva_vendor_create')
        data = {
            "businessname": "businessname",
            "email": "email",
            "phoneNumber": "phoneNumber",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_vendor(self):
        vendor = create_vendor()
        url = reverse('fva_vendor_detail', args=[vendor.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_vendor(self):
        vendor = create_vendor()
        data = {
            "businessname": "businessname",
            "email": "email",
            "phoneNumber": "phoneNumber",
        }
        url = reverse('fva_vendor_update', args=[vendor.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomerViewTest(unittest.TestCase):
    '''
    Tests for Customer
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customer(self):
        url = reverse('fva_customer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customer(self):
        url = reverse('fva_customer_create')
        data = {
            "firstname": "firstname",
            "lastname": "lastname",
            "email": "email",
            "phoneNumber": "phoneNumber",
            "amountOutstanding": "amountOutstanding",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customer(self):
        customer = create_customer()
        url = reverse('fva_customer_detail', args=[customer.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customer(self):
        customer = create_customer()
        data = {
            "firstname": "firstname",
            "lastname": "lastname",
            "email": "email",
            "phoneNumber": "phoneNumber",
            "amountOutstanding": "amountOutstanding",
        }
        url = reverse('fva_customer_update', args=[customer.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MenuViewTest(unittest.TestCase):
    '''
    Tests for Menu
    '''
    def setUp(self):
        self.client = Client()

    def test_list_menu(self):
        url = reverse('fva_menu_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_menu(self):
        url = reverse('fva_menu_create')
        data = {
            "name": "name",
            "description": "description",
            "price": "price",
            "quantity": "quantity",
            "isRecurring": "isRecurring",
            "frequencyOfReocurence": "frequencyOfReocurence",
            "vendorId": create_vendor().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_menu(self):
        menu = create_menu()
        url = reverse('fva_menu_detail', args=[menu.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_menu(self):
        menu = create_menu()
        data = {
            "name": "name",
            "description": "description",
            "price": "price",
            "quantity": "quantity",
            "isRecurring": "isRecurring",
            "frequencyOfReocurence": "frequencyOfReocurence",
            "vendorId": create_vendor().pk,
        }
        url = reverse('fva_menu_update', args=[menu.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OrderViewTest(unittest.TestCase):
    '''
    Tests for Order
    '''
    def setUp(self):
        self.client = Client()

    def test_list_order(self):
        url = reverse('fva_order_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        url = reverse('fva_order_create')
        data = {
            "description": "description",
            "itemsOrdered": "itemsOrdered",
            "amountDue": "amountDue",
            "amountPaid": "amountPaid",
            "amountOutstanding": "amountOutstanding",
            "vendorId": "vendorId",
            "orderStatus": "orderStatus",
            "menuId": "menuId",
            "customer": create_customer().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_order(self):
        order = create_order()
        url = reverse('fva_order_detail', args=[order.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_order(self):
        order = create_order()
        data = {
            "description": "description",
            "itemsOrdered": "itemsOrdered",
            "amountDue": "amountDue",
            "amountPaid": "amountPaid",
            "amountOutstanding": "amountOutstanding",
            "vendorId": "vendorId",
            "orderStatus": "orderStatus",
            "menuId": "menuId",
            "customerId": create_customer().pk,
        }
        url = reverse('fva_order_update', args=[order.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OrderStatusViewTest(unittest.TestCase):
    '''
    Tests for OrderStatus
    '''
    def setUp(self):
        self.client = Client()

    def test_list_orderstatus(self):
        url = reverse('fva_orderstatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_orderstatus(self):
        url = reverse('fva_orderstatus_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_orderstatus(self):
        orderstatus = create_orderstatus()
        url = reverse('fva_orderstatus_detail', args=[orderstatus.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_orderstatus(self):
        orderstatus = create_orderstatus()
        data = {
            "name": "name",
        }
        url = reverse('fva_orderstatus_update', args=[orderstatus.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class NotificationViewTest(unittest.TestCase):
    '''
    Tests for Notification
    '''
    def setUp(self):
        self.client = Client()

    def test_list_notification(self):
        url = reverse('fva_notification_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_notification(self):
        url = reverse('fva_notification_create')
        data = {
            "message": "message",
            "subjectUserId": "subjectUserId",
            "messageStatus": "messageStatus",
            "orderId": create_order().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_notification(self):
        notification = create_notification()
        url = reverse('fva_notification_detail', args=[notification.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_notification(self):
        notification = create_notification()
        data = {
            "message": "message",
            "subjectUserId": "subjectUserId",
            "messageStatus": "messageStatus",
            "orderId": create_order().pk,
        }
        url = reverse('fva_notification_update', args=[notification.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class MessageStatusViewTest(unittest.TestCase):
    '''
    Tests for MessageStatus
    '''
    def setUp(self):
        self.client = Client()

    def test_list_messagestatus(self):
        url = reverse('fva_messagestatus_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_messagestatus(self):
        url = reverse('fva_messagestatus_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_messagestatus(self):
        messagestatus = create_messagestatus()
        url = reverse('fva_messagestatus_detail', args=[messagestatus.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_messagestatus(self):
        messagestatus = create_messagestatus()
        data = {
            "name": "name",
        }
        url = reverse('fva_messagestatus_update', args=[messagestatus.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


