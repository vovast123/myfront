from multiprocessing import context
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.views.generic import ListView, UpdateView, DeleteView, View,CreateView
from django.contrib.auth.models import User
from django.http import Http404,HttpResponseRedirect
from django.core.paginator import Paginator
from .models import *

# Create your views here.
class Index(DeleteView):
    def get(self,request):
        new_post = Post.objects.all().order_by('-time')[:6]
        context={
            'new_post':new_post
        }
        return render(request,'base.html',context)


class All(ListView):
    def get(self,request):
        new_post = Post.objects.all().order_by('-time')
        post = Post.objects.all().order_by('-time')
        paginator = Paginator(post,6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context={
            'new_post':new_post,
            'page_obj':page_obj
        }
        return render(request,'allpost.html',context)


class Info(DeleteView):
    def get(self,request,post_id):
        new_post = Post.objects.get(id = post_id)
        context={
            'new_post':new_post
        }
        return render(request,'info.html',context)




class Common(DeleteView):
    def get(self,request):
        new_post = Post.objects.filter(rare = 'Common').order_by('-time')
        post = Post.objects.filter(rare = 'Common').order_by('-time')[:1]
        context={
            'new_post':new_post,
            'post':post
        }
        return render(request,'rare.html',context)

class Uncommon(DeleteView):
    def get(self,request):
        new_post = Post.objects.filter(rare = 'Uncommon').order_by('-time')
        post = Post.objects.filter(rare = 'Uncommon').order_by('-time')[:1]
        context={
            'new_post':new_post,
            'post':post
        }
        return render(request,'rare.html',context)
class Rare(DeleteView):
    def get(self,request):
        new_post = Post.objects.filter(rare = 'Rare').order_by('-time')
        post = Post.objects.filter(rare = 'Rare').order_by('-time')[:1]
        context={
            'new_post':new_post,
            'post':post
        }
        return render(request,'rare.html',context)
class Mythical(DeleteView):
    def get(self,request):
        new_post = Post.objects.filter(rare = 'Mythical').order_by('-time')
        post = Post.objects.filter(rare = 'Mythical').order_by('-time')[:1]
        context={
            'new_post':new_post,
            'post':post
        }
        return render(request,'rare.html',context)
class Legendary(DeleteView):
    def get(self,request):
        new_post = Post.objects.filter(rare = 'Legendary').order_by('-time')
        post = Post.objects.filter(rare = 'Legendary').order_by('-time')[:1]
        context={
            'new_post':new_post,
            'post':post
        }
        return render(request,'rare.html',context)
class Immortal(DeleteView):
    def get(self,request):
        new_post = Post.objects.filter(rare = 'Immortal').order_by('-time')
        post = Post.objects.filter(rare = 'Immortal').order_by('-time')[:1]
        context={
            'new_post':new_post,
            'post':post
        }
        return render(request,'rare.html',context)
class Arcana(DeleteView):
    def get(self,request):
        new_post = Post.objects.filter(rare = 'Arcana').order_by('-time')
        post = Post.objects.filter(rare = 'Arcana').order_by('-time')[:1]
        context={
            'new_post':new_post,
            'post':post
        }
        return render(request,'rare.html',context)
class Ancient(DeleteView):
    def get(self,request):
        new_post = Post.objects.filter(rare = 'Ancient').order_by('-time')
        post = Post.objects.filter(rare = 'Ancient').order_by('-time')[:1]
        context={
            'new_post':new_post,
            'post':post
        }
        return render(request,'rare.html',context)