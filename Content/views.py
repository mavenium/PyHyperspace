from django.http import JsonResponse
from django.shortcuts import render, redirect
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
    if request.is_ajax():
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        message = request.POST.get('message', None)
        if name is not None and email is not None and message is not None:

            models.ContactUs.objects.create(
                name=name,
                email=email,
                message=message
            )

            data = {
                'success': 'Your message has been saved successfully.'
            }

        else:
            data = {
                'error': 'Error inserting message!'
            }
        return JsonResponse(data)
    else:
        return redirect('Contact:index')
