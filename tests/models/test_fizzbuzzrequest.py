import pytest
from django.test import Client
from django.urls import reverse

from rest_fizzbuzz.models import FizzBuzzRequest
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

    client.get(reverse("my-fizz-buzz") + "?" + params)
    fizzbuzz_request = FizzBuzzRequest.get_most_popular()
    assert fizzbuzz_request.count == 1
    assert fizzbuzz_request.int1 == 3
    assert fizzbuzz_request.int2 == 5
    assert fizzbuzz_request.limit == 20
    assert fizzbuzz_request.string1 == "fizz"
    assert fizzbuzz_request.string2 == "buzz"
