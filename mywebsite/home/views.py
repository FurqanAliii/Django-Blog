from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
# def home(request):
#     # data={
#     #     'name':'Furqan Ali',
#     #     'class':'BS Software Engineering',
#     #     'RollNo':3092,
#     #     'courses':[]
#     # }

#     # posts=[
#     #     {
#     #         'title':'Python in Airtificial Intelligence',
#     #         'author':'Furqan Ali',
#     #         'content':'Python is programming language',
#     #         'date_posted':'August 12, 2026',
#     #     },
#     #     {
#     #         'title':'JAVA in Micorservices',
#     #         'author':'Furqan Ali',
#     #         'content':'Java  is helping enterprise level companies',
#     #         'date_posted':'August 12, 2026',
#     #     }
#     # ]
#     if request.method=='GET':
#         context={ 
#             'posts':Post.objects.all()
#         }
#         print(request.headers)
#         return render(request,'home/home.html',context)
#     else:
#         return HttpResponse('Posting Mr Baloch')
    


def about(request):
    print(request.method)
    return render(request,'home/about.html')


def contact(request):
    print(request.path)
    print(request.GET)
    return render(request,'home/contact.html')


def hello(request):
    print(request.user)
    return HttpResponse("Hello World!")


class HomeView(ListView):
    model= Post

    template_name='home/home.html'
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=4



class UserHomeView(ListView):
    model= Post

    template_name='home/user_posts.html'
    context_object_name='posts'
    paginate_by=4

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model=Post
    context_object_name='post'
    template_name='home/post-detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title', 'content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title', 'content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        # The view instance has access to self.request.user
        # Returns True if the user is a premium member, otherwise False
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        # The view instance has access to self.request.user
        # Returns True if the user is a premium member, otherwise False
        if self.request.user == post.author:
            return True
        return False



