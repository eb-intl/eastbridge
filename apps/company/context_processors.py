
from ..blog.models import Article
from .models import Office


def footer(request):
    office = Office.objects.filter(primary=True).first()
    news = Article.objects.filter().order_by('updated')[:3]
    return {'office': office, 'news': news}
