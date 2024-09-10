from django.shortcuts import render, get_object_or_404
from .models import Painting, Tag


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

def painting_detail(request, slug, id):
    painting = get_object_or_404(Painting, id=id, slug=slug)
    return render(request, 'shop/painting/detail.html', {'painting': painting})
