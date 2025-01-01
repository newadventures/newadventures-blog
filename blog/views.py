from django.utils import timezone
from django.views.generic import ListView, DetailView

from blog import models
from blog.mixins import ContextDataMixin, context_data


class ArticleListView(ListView):
    queryset = models.Article.objects.filter(published__lte=timezone.now()).order_by(
        "-published"
    )
    context_object_name = "articles"
    template_name = "blog/article_list.html"


class ArticleDetailView(ContextDataMixin, DetailView):
    queryset = models.Article.objects.filter(published__lte=timezone.now())
    context_object_name = "article"
    template_name = "blog/article_detail.html"

    @context_data(key="page_title")
    def get_page_name(self, request):
        if self.object is not None:
            return self.object.title
