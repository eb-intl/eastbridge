
from .models import Article, ArticleFile
from photologue.models import Photo


def blog(request):
    news = Article.objects.filter().order_by('updated')[:3]
    files = ArticleFile.objects.filter().order_by('id')[:10]
    default_image = Photo.objects.get(slug='default')
    return {'news': news, 'files': files, 'default_image': default_image}
