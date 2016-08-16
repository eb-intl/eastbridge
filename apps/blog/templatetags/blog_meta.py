from django import template
from django.db.models.query import QuerySet

from ..models import Article

register = template.Library()


@register.filter(name='short_keywords')
def short_keywords(objs):
    words = []
    if isinstance(objs, QuerySet):
        for obj in objs:
            for tag in obj.tags.all():
                words.append(tag.short_name)
    else:
        for tag in objs.tags.all():
            words.append(tag.short_name)

    cwords = list(set(words))
    return ','.join(cwords)


@register.filter(name='long_keywords')
def long_keywords(objs):
    words = []
    if isinstance(objs, QuerySet):
        for obj in objs:
            for tag in obj.tags.all():
                words.append(tag.long_name)
    else:
        for tag in objs.tags.all():
            words.append(tag.long_name)

    cwords = list(set(words))
    return ','.join(cwords)
