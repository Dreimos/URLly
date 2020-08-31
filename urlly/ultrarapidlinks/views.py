from django.views.generic import CreateView, DetailView, RedirectView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import StoredURL
from .serializers import StoredURLSerializer

class URLCreateView(LoginRequiredMixin, CreateView):
    model = StoredURL
    fields = ['url', 'descriptor']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class URLListView(LoginRequiredMixin, ListView):
    model = StoredURL
    queryset = StoredURL.objects.all()

    def get_queryset(self):
        return StoredURL.objects.filter(creator=self.request.user).order_by("created").reverse()

class URLDetailView(LoginRequiredMixin, DetailView):
    model = StoredURL
    fields = ['url', 'descriptor', 'slug']

class URLRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = "redirect"

    def get_redirect_url(self, *args, **kwargs):
        url_object = get_object_or_404(StoredURL, slug=kwargs["slug"])
        url_object.counter += 1
        url_object.save() 
        return url_object.url

class URLUpdateView(LoginRequiredMixin, UpdateView):
    model = StoredURL
    fields = ['url', 'descriptor']
    action = "Update"

# REST addition.

class StoredURLAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        url = get_object_or_404(StoredURL, slug=kwargs["slug"])
        serializer = StoredURLSerializer(url, many=False)
        return Response(serializer.data)
