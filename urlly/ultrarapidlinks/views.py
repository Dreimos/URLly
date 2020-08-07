from django.views.generic import CreateView, DetailView, RedirectView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import StoredURL

class URLCreateView(LoginRequiredMixin, CreateView):
    model = StoredURL
    fields = ['url']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class URLListView(LoginRequiredMixin, ListView):
    model = StoredURL
    queryset = StoredURL.objects.all()

    def get_queryset(self):
        return StoredURL.objects.filter(creator=self.request.user)

class URLDetailView(LoginRequiredMixin, DetailView):
    model = StoredURL
    fields = ['url', 'slug']

class URLRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = "redirect"

    def get_redirect_url(self, *args, **kwargs):
        url_object = get_object_or_404(StoredURL, slug=kwargs["slug"])
        return url_object.url
