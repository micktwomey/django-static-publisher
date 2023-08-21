from django.http import HttpResponse
from django.db.models.query import QuerySet
from django.urls import reverse

from typing import Callable, Any, Iterable

ViewCallable = Callable[..., HttpResponse]

QueryCallable = Callable[[], QuerySet]

Reverser = Callable[[Any], str]


# TODO: using a generic class based view doesn't seem to reverse
# TODO: is this a good name?
def reverser(
    view: str | ViewCallable,
    args: Iterable[str] | None = None,
    kwargs: Iterable[str] | None = None,
) -> Reverser:
    """Returns a callable used to reverse a model into a url using the given view
    Useful if you don't need any logic beyond looking up the args and kwargs for the
    reverse() call.
    """
    args = args if args is not None else []
    kwargs = kwargs if kwargs is not None else []

    def reverse_model(model: Any) -> str:
        reverse_args = [getattr(model, arg) for arg in args]
        reverse_kwargs = {k: getattr(model, k) for k in kwargs}
        return reverse(view, args=reverse_args, kwargs=reverse_kwargs)

    return reverse_model


# TODO: create a proper registry?
Patterns = list[tuple[QueryCallable | None, Reverser]]
PATTERNS: Patterns = []


# TODO: is this a good name?
def pattern(
    query: QueryCallable | None,
    reverser: Reverser,
):
    """Registers a query and view for generating static content"""
    PATTERNS.append((query, reverser))
