from django_static_publisher.patterns import pattern, reverser

from . import views

patterns = [
    pattern(query=None, reverser=reverser(view="articles:index")),
    pattern(
        query=views.ArticleView().get_queryset,
        reverser=reverser(view="articles:article", args=["slug"]),
    ),
]
