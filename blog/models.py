from __future__ import annotations

from typing import Optional, Any

import markdown

from django.db import models
from django.db.models import signals
from django.urls import reverse
from django.utils.html import strip_tags


class Tag(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Article(models.Model):
    title = models.CharField(
        max_length=100,
    )
    slug = models.SlugField()
    tldr = models.TextField()
    content = models.TextField()
    published = models.DateTimeField(
        null=True,
        blank=True,
    )
    html_content = models.TextField(
        editable=False,
    )
    html_tldr = models.TextField(
        editable=False,
    )
    tags = models.ManyToManyField(
        to="blog.Tag",
        blank=True,
        related_name="articles",
    )

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self) -> str:
        return reverse("blog:article-detail", kwargs={"slug": self.slug})

    @classmethod
    def pre_save(
        cls, sender: Article, instance: Article, **kwargs: Optional[Any]
    ) -> None:
        instance.generate_html_content()

    def generate_html_content(self) -> None:
        self.html_content = markdown.markdown(self.content)
        self.html_tldr = markdown.markdown(self.tldr)


    @property
    def meta_description(self) -> str:
        return strip_tags(self.html_tldr)

signals.pre_save.connect(receiver=Article.pre_save, sender=Article)
