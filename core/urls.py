from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rfq/', include('rfq.urls')),
    path('api/', include('contacts.urls')),
]


