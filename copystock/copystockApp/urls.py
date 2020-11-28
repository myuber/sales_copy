from django.urls import path
from . import views

app_name = "copystockApp"

urlpatterns = [
    path("top/", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("article/<int:pk>/", views.view_article, name="view_article"),
    path("article/<int:pk>/edit/", views.edit, name="edit"),
    path("article/<int:pk>/delete/", views.delete, name="delete"),
]
