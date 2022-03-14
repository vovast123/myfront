from email.policy import default
from django.db import models
from django.forms import ImageField
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User



class Post(models.Model):
    RARE_OF_ITEM_CHOICES = [
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
        ('Mythical', 'Mythical'),
        ('Legendary', 'Legendary'),
        ('Immortal', 'Immortal'),
        ('Arcana', 'Arcana'),
        ('Ancient', 'Ancient'),
    ]
    
    image = models.ImageField('Image')
    name = models.CharField('Название',max_length=250)
    rare = models.CharField('Редкость',choices=RARE_OF_ITEM_CHOICES,max_length=100)
    text = models.TextField('Описание')
    price = models.PositiveIntegerField('Ценна',default=0)
    hero = models.CharField('Герой',max_length=155)
    time = models.DateTimeField('time', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'скин'
        verbose_name_plural = 'скины'













