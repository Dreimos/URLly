from django.urls import path

from .views import URLCreateView, URLDetailView, URLRedirectView, URLListView

app_name = "ultrarapidlinks"
urlpatterns = [
    path("", view=URLCreateView.as_view(), name="create"),
    path("detail/<str:slug>", view=URLDetailView.as_view(), name="detail"),
    path("redirect/<str:slug>", view=URLRedirectView.as_view(), name="redirect"),
    path("list/", view=URLListView.as_view(), name="list")
]
