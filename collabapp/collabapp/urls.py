from django.contrib import admin
from django.urls import path, include 
# from uploads.views import uploads, singleUpload


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('uploads.urls'))
]
