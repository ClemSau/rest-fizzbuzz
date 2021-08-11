import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status

from tests.utils import make_params

client = Client()


@pytest.mark.django_db
def test_valid_my_fizzbuzz(client: Client):
    params = make_params(
        int1=3,
        int2=5,
        limit=20,
        string1="fizz",
        string2="buzz",
    )

    response = client.get(reverse("my-fizz-buzz") + "?" + params)
    assert response.status_code == status.HTTP_200_OK
