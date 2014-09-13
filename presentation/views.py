#-*- coding: utf-8 -*-
from django.shortcuts import render
from models import Offer
from api import get_offers
from django.http import Http404

# Create your views here.


def accueil(request):
    """ Accueil du site """
    return render(request, 'presentation/accueil.html', {})


def services(request):
    """ Presentation de l'entreprise """
    return render(request, 'presentation/services.html', {})


def offres(request):

    """ Offres et services """

    try:
        offers = get_offers()
    except Offer.DoesNotExist:
        raise Http404

    return render(request, 'presentation/offres.html', {'offers': offers})


def contact(request):
    """ Nous joindre """
    return render(request, 'presentation/contact.html', {})