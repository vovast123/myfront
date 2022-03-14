from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index.as_view(),name ='base'),
    path('Immortal/',views.Immortal.as_view(),name='immortal'),
    path('Arcana/',views.Arcana.as_view(),name='arcana'),
    path('Common/',views.Common.as_view(),name='common'),
    path('Uncommon/',views.Uncommon.as_view(),name='uncommon'),
    path('Rare/',views.Rare.as_view(),name='rare'),
    path('Mythical/',views.Mythical.as_view(),name='mythical'),
    path('Legendary/',views.Legendary.as_view(),name='legendary'),
    path('Ancient/',views.Ancient.as_view(),name='ancient'),
    path('<int:post_id>', views.Info.as_view(),name ='info'),
    path('All-skins/', views.All.as_view(),name ='all'),
]