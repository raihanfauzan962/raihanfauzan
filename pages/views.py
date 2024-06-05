from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"
    
class LifePageView(TemplateView):
    template_name = "life.html"
    
class ProjectsPageView(TemplateView):
    template_name = "projects.html"

class WorksPageView(TemplateView):
    template_name = "works.html"