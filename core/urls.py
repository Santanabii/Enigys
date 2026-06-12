from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

def test_view(request):
    return HttpResponse("API is working!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rfq/', include('rfq.urls')),
    path('api/', include('contacts.urls')),
]


