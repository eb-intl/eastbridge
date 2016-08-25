from django import template
from django.db.models.query import QuerySet

register = template.Library()


@register.filter(name='keywords')
def keywords(objs):
    words = []
    if isinstance(objs, QuerySet):
        for obj in objs:
            for tag in obj.tags.all():
                if len(tag.long_name) > 0:
                    words.append(tag.long_name)
                if len(tag.short_name) > 0:
                    words.append(tag.short_name)
    else:
        for tag in objs.tags.all():
            if len(tag.long_name) > 0:
                words.append(tag.long_name)
            if len(tag.short_name) > 0:
                words.append(tag.short_name)

    cwords = list(set(words))
    return ','.join(cwords)