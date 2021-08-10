from django.db import models


class FizzBuzzRequest(models.Model):
    """
    FizzBuzzRequest Model is used to count the number of requests on the my-fizz-buzz endpoint

    One instance is created for each unique combination of

    Each time a request is called in the /my-fizzbuzz endpoint, its count will be increased by 1
    """

    count = models.IntegerField(default=0)
    int1 = models.IntegerField()
    int2 = models.IntegerField()
    limit = models.IntegerField()
    string1 = models.CharField(max_length=200)
    string2 = models.CharField(max_length=200)

    @classmethod
    def get_most_popular(cls):
        try:
            return cls.objects.all().order_by("-count")[0]
        except IndexError:
            return None
