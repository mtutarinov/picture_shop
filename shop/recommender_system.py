import redis
from django.conf import settings

from .models import Painting

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)

def increase_rating(painting_id):
    r.zincrby('painting_views', 1, painting_id)


def most_view(exclude_list):
    painting_views = r.zrange('painting_views', 0, -1,
                              desc=True)[:10]
    painting_views_ids = [int(id) for id in painting_views]
    result = list(Painting.objects.filter(id__in=painting_views_ids).exclude(id__in=exclude_list))
    result.sort(key=lambda x: painting_views_ids.index(x.id))
    return result
