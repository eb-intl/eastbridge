from django import template
from django.db.models.query import QuerySet

register = template.Library()


@register.filter(name='keywords')
def keywords(objs):
    words = []
    if isinstance(objs, QuerySet):
        for obj in objs:
            for tag in obj.tags.all():
                words.append(tag.short_name)
                words.append(tag.long_name)
    else:
        for tag in objs.tags.all():
            words.append(tag.short_name)
            words.append(tag.long_name)

    cwords = list(set(words))
    return ','.join(cwords)