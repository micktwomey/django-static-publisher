from django.views import generic

from .models import Article


class IndexView(generic.ListView):
    template_name = "articles/index.html"
    context_object_name = "latest_articles_list"

    def get_queryset(self):
        return Article.objects.filter(published=True).order_by("-modified_date")[:5]


class ArticleView(generic.DetailView):
    model = Article
    template_name = "articles/article.html"

    def get_queryset(self):
        return Article.objects.filter(published=True)
