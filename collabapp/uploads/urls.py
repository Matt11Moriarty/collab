from django.urls import path
from . import views

urlpatterns = [
    # path("", views.blah, name="blah"),
    path("uploads/", views.uploads, name="uploads"),
    path("upload/<str:pk>", views.singleUpload, name="single upload")
]