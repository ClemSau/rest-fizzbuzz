# def setup_test_environment():
#     import os
#
#     import django
#
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rest_fizzbuzz.settings")
#     django.setup()


def make_params(**params):
    return "&".join([f"{k}={v}" for k, v in params.items()])
