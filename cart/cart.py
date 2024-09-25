from django.conf import settings
from shop.models import Painting


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, painting):
        painting_id = str(painting.id)
        if painting_id not in self.cart:
            self.cart[painting_id] = {'price': str(painting.price)}
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, painting):
        painting_id = str(painting.id)
        if painting_id in self.cart:
            del self.cart[painting_id]
            self.save()

    def __iter__(self):
        painting_ids = self.cart.keys()
        paintings = Painting.objects.filter(id__in=painting_ids)
        cart = self.cart.copy()
        for painting in paintings:
            cart[str(painting.id)]['painting'] = painting
        for item in cart.values():
            item['price'] = int(item['price'])
            yield item

    def __len__(self):
        return len(self.cart.values())

    def get_total_price(self):
        return sum(int(item['price']) for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()