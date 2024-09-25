import redis
from django.conf import settings

from django.shortcuts import render, get_object_or_404
from .models import Painting, Tag


r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


def painting_list(request, tag_slug=None):
    tag = None
    tags = Tag.objects.all()
    paintings = Painting.objects.filter(available=True)
    if tag_slug:
        tag = get_object_or_404(Tag,
                                slug=tag_slug)
        paintings = paintings.filter(tag=tag)
    return render(request,
                  'shop/painting/list.html',
                  {'tag': tag,
                   'tags': tags, 'paintings': paintings})


def painting_detail(request, id, slug):
    painting = get_object_or_404(Painting, id=id, slug=slug)
    r.zincrby('painting_views', 1, painting.id)
    painting_views = r.zrange('painting_views', 0, -1,
                             desc=True)[:10]
    painting_views_ids = [int(id) for id in painting_views]
    most_view = list(Painting.objects.filter(id__in=painting_views_ids).exclude(id=id))
    most_view.sort(key=lambda x:painting_views_ids.index(x.id))
    return render(request, 'shop/painting/detail.html',
                  {'painting': painting, 'most_view': most_view})
