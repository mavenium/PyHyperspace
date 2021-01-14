from django.shortcuts import render
from django.views import View

from . import models


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'blogs': models.Blog.objects.all()[:4]
        }
        return render(request, self.template_name, context)

