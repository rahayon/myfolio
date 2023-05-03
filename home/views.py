from home.models import MyProject, MyService
from django.shortcuts import render
from django.views.generic import View
from blog.models import Post
# Create your views here.
class HomeView(View):
    def get(self, request):
        carousel_posts = Post.objects.all().order_by('-id')[:4]
        services = MyService.objects.all()
        projects = MyProject.objects.all()[:3]
        context = {
            'posts': carousel_posts,
            'services': services,
            'projects': projects
        }
        return render(request, 'home/index.html',context)