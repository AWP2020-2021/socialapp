from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import (
    DetailView, ListView,
    TemplateView
)

from app.models import Post

# def index(request):
#     return HttpResponse("Welcome to the SocialApp!")

def index(request):
    post_list = Post.objects.all()
    return render(request, 'index.html', {'post_list': post_list})


class PostListView(View):

    def get(self, request, *args, **kwargs):
        post_list = Post.objects.all()
        return render(request, 'index.html', {'post_list': post_list})


# class PostListView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self):
#         post_list = Post.objects.all()
#         context = {
#             'post_list': post_list
#         }
#         return context


# class PostListView(ListView):
#     template_name = 'index.html'
#     model = Post
#     context_object_name = 'post_list'


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "post_detail.html", {"post": post})

class PostDetail(DetailView):
    model=Post
    template_name="post_detail.html"

class UserProfileView(TemplateView):
    template_name = 'user_profile.html'