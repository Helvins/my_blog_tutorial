from django.conf.urls import include, url
from article.views import home

urlpatterns = [
    url(r'^home/', home),
]
