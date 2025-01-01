from django.contrib import admin

from blog import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )
    prepopulated_fields = {"slug": ["name"]}


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "published",
    )
    prepopulated_fields = {"slug": ["title"]}
    readonly_fields = ("html_content",)
