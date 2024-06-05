from django.urls import path

from .views import HomePageView, WorksPageView, LifePageView, ProjectsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("life/", LifePageView.as_view(), name="life"),
    path("projects/", ProjectsPageView.as_view(), name="projects"),
    path("works/", WorksPageView.as_view(), name="works"),
]