from models import Offer


def get_offers():
    offers = Offer.objects.all()
    return offers

