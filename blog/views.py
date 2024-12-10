from django.shortcuts import render
from .models import Blog
from django.views.generic import TemplateView
def blog_list_view(request):
   bloglist = Blog.objects.all()

   context = {
       'bloglist': bloglist
   }

   return render(request, 'home.html', context)

def blog_detail_view(request, id):
    blog = Blog.objects.get(id=id)

    cotext = {
        'blog': blog
    }
    return render(request, 'detail.html', context=cotext)