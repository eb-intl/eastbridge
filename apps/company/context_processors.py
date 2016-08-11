
from ..blog.models import Article
from .models import Office


def footer(request):
    office = Office.objects.filter(primary=True).first()
    return {'office': office}
