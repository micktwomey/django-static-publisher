"""Static publishing config

"""

from django_static_publisher.patterns import pattern, reverser

from . import views
from . import models

from django.db.models.query import QuerySet
from django.urls import reverse


def detail_query() -> QuerySet:
    return models.Question.objects.order_by("-pub_date")


def reverse_results(model: models.Question) -> str:
    return reverse("polls:results", kwargs={"pk": model.pk})


patterns = [
    pattern(
        query=None, reverser=reverser(view="polls:index")
    ),  # Example using a view with no args
    pattern(
        query=detail_query, reverser=reverser(view="polls:detail", args=["pk"])
    ),  # Example using a view with one arg
    pattern(
        query=lambda: models.Question.objects,
        reverser=reverse_results,
    ),  # Example using our own reverse function
]
