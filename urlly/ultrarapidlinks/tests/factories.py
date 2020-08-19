from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import StoredURL
from urlly.users.tests.factories import UserFactory

import pytest

@pytest.fixture
def factory_url():
    return StoredURLFactory()

class StoredURLFactory(factory.django.DjangoModelFactory):
    url = factory.fuzzy.FuzzyText()
    creator = factory.SubFactory(UserFactory)
    class Meta:
        model = StoredURL
