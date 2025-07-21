from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    path("add-dare", views.create_dare, name="create_dare"),

    path("delete-dare/<int:id>", views.delete_dare, name="delete_dare"),

    path("edit_dare/<int:id>", views.edit_dare, name="edit_dare"),
]

