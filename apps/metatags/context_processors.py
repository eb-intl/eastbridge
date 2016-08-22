from .models import Tag


def metatags(request):
    tags = Tag.objects.filter()
    return {'tags': tags}
