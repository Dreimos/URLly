import pytest
from pytest_django.asserts import assertContains, assertRedirects

from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory

from urlly.users.models import User
from ..models import StoredURL
from ..views import URLCreateView, URLUpdateView, URLDetailView, URLListView, URLRedirectView
from .factories import factory_url, StoredURLFactory

pytestmark = pytest.mark.django_db

def test_URLListView(rf, admin_user):
    request = rf.get(reverse("ultrarapidlinks:list"))
    request.user = admin_user
    response = URLListView.as_view()(request)
    assertContains(response, "Link List")

def test_URLDetailView(rf, factory_url, admin_user):
    request = rf.get(reverse("ultrarapidlinks:detail", kwargs={'slug':factory_url.slug}))
    request.user = admin_user
    response = URLDetailView.as_view()(request, slug=factory_url.slug)
    assertContains(response, "Url Detail")

def test_URLCreateView(rf, factory_url, admin_user):
    request = rf.get(reverse("ultrarapidlinks:create"))
    request.user = admin_user
    response = URLCreateView.as_view()(request)
    assert response.status_code == 200