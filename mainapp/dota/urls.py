from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(),name ='base'),
    path("filter/",views.RareView.as_view(),name="filter"),
    path("<slug:slug>/",views.PostDetailView.as_view(),name = "post_detail"),

]