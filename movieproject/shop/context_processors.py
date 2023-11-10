from .models import Category
def menu_links(request):
    my_links = Category.objects.all()
    return dict(links=my_links)