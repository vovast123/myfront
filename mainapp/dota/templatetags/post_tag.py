from django import template

from dota.models import Rare

register = template.Library()


@register.simple_tag()
def get_rare():
    return Rare.objects.all()