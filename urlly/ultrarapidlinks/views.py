from django.views.generic import CreateView, DetailView, RedirectView

from .models import StoredURL

class URLCreateView(CreateView):
    model = StoredURL
    fields = ['url']

class URLDetailView(DetailView):
    model = StoredURL
    fields = ['url', 'slug']

