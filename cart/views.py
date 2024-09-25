import redis
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Painting
from .cart import Cart

# from .forms import CartAddPaintingForm

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


@require_POST
def cart_add(request, painting_id):
    cart = Cart(request)
    painting = get_object_or_404(Painting, id=painting_id)
    cart.add(painting=painting)
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, painting_id):
    cart = Cart(request)
    painting = get_object_or_404(Painting, id=painting_id)
    cart.remove(painting)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    cart_paintings = [item['painting'] for item in cart]
    cart_paintings_ids = [painting.id for painting in cart_paintings]
    painting_views = r.zrange('painting_views', 0, -1,
                              desc=True)[:10]
    painting_views_ids = [int(id) for id in painting_views]
    most_view = list(Painting.objects.filter(id__in=painting_views_ids).exclude(id__in=cart_paintings_ids))
    most_view.sort(key=lambda x: painting_views_ids.index(x.id))
    return render(request, 'cart/detail.html', {'cart': cart, 'most_view': most_view})
