from django.shortcuts import render
from django.views import View, generic

from . import models


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'blogs': models.Blog.objects.all()[:4],
            'skills': models.Skill.objects.all()[:6]
        }
        return render(request, self.template_name, context)


class BlogSingle(generic.DetailView):
    model = models.Blog
    template_name = 'blog_single.html'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])


def create_contact(request):
    pass
