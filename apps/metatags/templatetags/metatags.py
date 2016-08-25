from django import template
from django.db.models.query import QuerySet

from .. models import Tag

register = template.Library()


@register.filter(name='keywords')
def keywords(objs=None):
    words = []
    if isinstance(objs, QuerySet):
        for obj in objs:
            if hasattr(obj, 'tags'):
                for tag in obj.tags.all():
                    if len(tag.long_name) > 0:
                        words.append(tag.long_name)
                    if len(tag.short_name) > 0:
                        words.append(tag.short_name)
    elif objs:
        if hasattr(objs, 'tags'):
            for tag in objs.tags.all():
                if len(tag.long_name) > 0:
                    words.append(tag.long_name)
                if len(tag.short_name) > 0:
                    words.append(tag.short_name)
    else:
        tags = Tag.objects.all()
        for tag in tags:
            if len(tag.long_name) > 0:
                words.append(tag.long_name)
            if len(tag.short_name) > 0:
                words.append(tag.short_name)

    cwords = list(set(words))
    return ','.join(cwords)