from cgitb import text
from email.policy import default
from django.db import models
from django.forms import ImageField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Rare(models.Model):
    name = models.CharField('Название',max_length=250)
    rare = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'редкость'
        verbose_name_plural = 'редкость'
class Post(models.Model):
    image = models.ImageField('Image')
    name = models.CharField('Название',max_length=250)
    rare = models.ForeignKey(Rare,verbose_name="редкость",related_name="hero_rare",on_delete=models.SET_NULL,null=True )
    text = models.TextField('Описание')
    price = models.PositiveIntegerField('Ценна',default=0)
    hero = models.CharField('Герой',max_length=155)
    time = models.DateTimeField('time', default=timezone.now)
    url = models.SlugField(max_length=130, unique=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug":self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'скин'
        verbose_name_plural = 'скины'

    














