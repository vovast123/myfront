from multiprocessing import context
from re import template
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.views.generic import ListView, UpdateView, DeleteView, View,CreateView,DetailView
from django.contrib.auth.models import User
from django.http import Http404,HttpResponseRedirect
from django.core.paginator import Paginator
from .models import *

class IndexView(ListView):
    model = Post
    paginate_by = 6
    queryset = Post.objects.all().order_by("-time")

class PostDetailView(DetailView):
        #detail one
    model = Post 
    slug_field = 'url'
    context_object_name = "new_post"


class RareView(ListView):
    def get_queryset(self):
        queryset = Post.objects.filter(
            rare__in=self.request.GET.getlist("rare")
            )

        return queryset