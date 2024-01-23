from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.ListLinks.as_view(), name="list_links"),
    path("create/", views.CreateLink.as_view(), name="create_link"),
    path("delete/<int:link_id>/", views.DeleteLink.as_view(), name="delete_link"),
    path("<str:short_url>/", views.Redirect.as_view(), name="redirect"),
]
