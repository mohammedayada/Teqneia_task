from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RepositoryList

urlpatterns = [
    # get top 3 Repositories
    path("top-repositories", RepositoryList.as_view(), name="top-repositories"),

]