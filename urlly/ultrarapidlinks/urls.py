from django.urls import path

from .views import URLCreateView, URLDetailView

app_name = "ultrarapidlinks"
urlpatterns = [
    path("", view=URLCreateView.as_view(), name="create"),
    path("detail/<str:slug>", view=URLDetailView.as_view(), name="detail"),
]
