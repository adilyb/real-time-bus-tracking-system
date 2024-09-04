from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("bts_app.urls")),
    path('accounts/', include('accounts.urls')),
    path("admin/", admin.site.urls),
    
]

