import pytest

pytestmark = pytest.mark.django_db

from ..models import StoredURL, slug_save
from .factories import StoredURLFactory

def test__str__():
    url = StoredURLFactory()
    assert url.__str__() == str(url.url)
    assert str(url) == str(url.url)

def test_get_absolute_url():
    stored_url = StoredURLFactory()
    url = stored_url.get_absolute_url()
    assert url == f"/ultrarapidlinks/detail/{stored_url.slug}/"

def test_slug_generation():
    url1 = StoredURLFactory()
    url2 = StoredURLFactory()
    assert url1.slug != url2.slug
