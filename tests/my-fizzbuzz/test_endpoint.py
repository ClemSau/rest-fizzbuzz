from django.test import Client
from tests.utils import make_params
from rest_framework import status
from django.urls import reverse
from tests.utils import setup_test_environment

setup_test_environment()


def test_valid_my_fizzbuzz():
    params = make_params(
        int1=3,
        int2=5,
        limit=10,
        string1="fizz",
        string2="buzz",
    )

    response = Client().get(reverse("my-fizz-buzz") + "?" + params)
    assert response.status_code == status.HTTP_200_OK
