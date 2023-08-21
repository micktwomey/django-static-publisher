from django.contrib import admin

from . import models


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    list_display = ["title", "slug", "published", "modified_date"]
    list_filter = ["published", "created_date", "modified_date"]
    search_fields = ["title", "content", "slug"]
