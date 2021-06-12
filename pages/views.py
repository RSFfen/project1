from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView): # new
    template_name = 'about.html'

class House1PageView(TemplateView):
    template_name = 'house1.html'

class House2PageView(TemplateView):
    template_name = 'house2.html'

class House3PageView(TemplateView):
    template_name = 'house3.html'
