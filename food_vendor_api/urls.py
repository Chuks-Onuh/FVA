from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Food Vendor Api'
API_DESCRIPTION = 'A Web Api for Food Vendors'
schema_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    
    path('api/v1/account/', include('allauth.urls')),
    path('api/v1/accounts-rest/registration/account-confirm-email/<int:pk>/', confirm_email, name='account_confirm_email'),

    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('', schema_view),
]