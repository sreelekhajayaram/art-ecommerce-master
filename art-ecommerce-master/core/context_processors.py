from django.apps import apps


def categories(request):
    if apps.is_installed('shop'):
        Category = apps.get_model('shop', 'Category')
        return {'nav_categories': Category.objects.all()}
    return {'nav_categories': []}


def cart_count(request):
    if request.user.is_authenticated and apps.is_installed('shop'):
        CartItem = apps.get_model('shop', 'CartItem')
        return {'cart_count': CartItem.objects.filter(user=request.user).count()}
    return {'cart_count': 0}

