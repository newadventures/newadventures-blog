from django.urls import path

from blog import views

app_name = "blog"
urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article-list"),
    path("<slug:slug>/", views.ArticleDetailView.as_view(), name="article-detail"),
]
