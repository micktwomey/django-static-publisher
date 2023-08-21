from django_static_publisher.patterns import pattern, reverser


patterns = [
    pattern(query=None, reverser=reverser(view="index")),
]
