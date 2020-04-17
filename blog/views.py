from django.views.generic import TemplateView, ListView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from . import views

from .models import Blog

# Create your views here.

    

# Create your views here.
# Create your views here.

def allblogs(request):
    blogs = Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def detail(request,blog_id):
    detailblog=get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':detailblog})


class HomePageView(TemplateView):
    template_name = 'searchhome.html'


class SearchResultsView(ListView):
    model = Blog
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Blog.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return object_list


