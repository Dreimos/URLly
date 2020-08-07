from django.urls import path

from .views import URLCreateView, URLUpdateView, URLDetailView, URLRedirectView, URLListView

app_name = "ultrarapidlinks"
urlpatterns = [
    path("", view=URLCreateView.as_view(), name="create"),
    path("list/", view=URLListView.as_view(), name="list"),
    path("detail/<slug:slug>/", view=URLDetailView.as_view(), name="detail"),
    path("update/<slug:slug>/", view=URLUpdateView.as_view(), name="update"),
    path("<slug:slug>/", view=URLRedirectView.as_view(), name="redirect"),
]
