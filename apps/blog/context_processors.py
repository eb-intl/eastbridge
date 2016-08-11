
from .models import Article, ArticleFile


def blog(request):
    news = Article.objects.filter().order_by('updated')[:3]
    files = ArticleFile.objects.filter().order_by('id')[:10]
    return {'news': news, 'files': files}
