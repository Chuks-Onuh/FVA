from django.urls import path, include
from . import views

urlpatterns = (
    # urls for Vendor
    path('fva/vendor/', views.VendorListView.as_view(), name='fva_vendor_list'),
    path('fva/vendor/create/', views.VendorCreateView.as_view(), name='fva_vendor_create'),
    path('fva/vendor/rud/<int:pk>/', views.VendorRUDView.as_view(), name='fva_vendor_detail'),
)

urlpatterns += (
    # urls for Customer
    path('fva/customer/', views.CustomerListView.as_view(), name='fva_customer_list'),
    path('fva/customer/create/', views.CustomerCreateView.as_view(), name='fva_customer_create'),
    path('fva/customer/rud/<int:pk>/', views.CustomerRUDView.as_view(), name='fva_customer_detail'),
)

urlpatterns += (
    # urls for Menu
    path('fva/menu/', views.MenuListView.as_view(), name='fva_menu_list'),
    path('fva/menu/create/', views.MenuCreateView.as_view(), name='fva_menu_create'),
    path('fva/menu/rud/<int:pk>/', views.MenuRUDView.as_view(), name='fva_menu_detail'),
)

urlpatterns += (
    # urls for Order
    path('fva/order/', views.OrderListView.as_view(), name='fva_order_list'),
    path('fva/order/create/', views.OrderCreateView.as_view(), name='fva_order_create'),
    path('fva/order/rud/<int:pk>/', views.OrderRUDView.as_view(), name='fva_order_detail'),
)

urlpatterns += (
    # urls for OrderStatus
    path('fva/orderstatus/', views.OrderStatusListView.as_view(), name='fva_orderstatus_list'),
    path('fva/orderstatus/create/', views.OrderStatusCreateView.as_view(), name='fva_orderstatus_create'),
    path('fva/orderstatus/rud/<int:pk>/', views.OrderStatusRUDView.as_view(), name='fva_orderstatus_detail'),
)

urlpatterns += (
    # urls for Notification
    path('fva/notification/', views.NotificationListView.as_view(), name='fva_notification_list'),
    path('fva/notification/create/', views.NotificationCreateView.as_view(), name='fva_notification_create'),
    path('fva/notification/rud/<int:pk>/', views.NotificationRUDView.as_view(), name='fva_notification_detail'),
)

urlpatterns += (
    # urls for MessageStatus
    path('fva/messagestatus/', views.MessageStatusListView.as_view(), name='fva_messagestatus_list'),
    path('fva/messagestatus/create/', views.MessageStatusCreateView.as_view(), name='fva_messagestatus_create'),
    path('fva/messagestatus/rud/<int:pk>/', views.MessageStatusRUDView.as_view(), name='fva_messagestatus_detail'),
)

