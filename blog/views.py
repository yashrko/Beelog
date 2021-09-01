from blog.models import Article
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.forms import ImageField

# Create your views here.
class Home_view(ListView):
    model=Article
    template_name='home.html'
    ordering=['-date_posted']

class Blog_detailview(LoginRequiredMixin,DetailView):
    model=Article
    template_name='blogdetail.html'  
    # def test_func(self):
    #      article=self.get_object()
    #      if(self.request.user==article.author):
    #          return True
    #      else:
    #          return False  

class Blog_createview(LoginRequiredMixin,CreateView):
    model=Article
    template_name='createblog.html'
    fields=['title','description','article_image']
    # widgets = {
    #         'article_image': ImageField(required=True),
    #     }
    success_url="/home"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
    # def test_func(self):
    #      article=self.get_object()
    #      if(self.request.user==article.author):
    #          return True
    #      else:
    #          return False    
class Blog_updateview(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Article
    template_name='createblog.html'
    fields=['title','description','article_image']
    success_url="../"
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)   
             
    def test_func(self):
         article=self.get_object()
         if(self.request.user==article.author):
             return True
         else:
             return False    

class Blog_deleteview(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Article
    template_name='deleteblog.html'
    success_url="../../"
    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form) 
    def test_func(self):
         article=self.get_object()
         if(self.request.user==article.author):
             return True
         else:
             return False