from django.views.generic import TemplateView, CreateView
from .models import Comment


class HomePageView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'all_comments_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_comments_list'] = Comment.objects.all()
        return context


class AboutPageView(TemplateView): # new
    template_name = 'about.html'

class House1PageView(TemplateView):
    template_name = 'house1.html'

class House2PageView(TemplateView):
    template_name = 'house2.html'

class House3PageView(TemplateView):
    template_name = 'house3.html'

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('text',)