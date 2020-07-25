from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('cycle/', include('cycle.urls', namespace='cycle')),
    path('admin/', admin.site.urls),
]