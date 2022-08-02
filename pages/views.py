from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import prices, bedrooms, states

def index(request):
    listings = Listing.objects.all().filter(is_published=True)[:3]

    context = {
        "listings": listings,
        "states": states,
        "bedrooms": bedrooms,
        "prices": prices
    }

    return render(request, "pages/index.html", context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.all()

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        "realtors": realtors,
        "mvp_realtors": mvp_realtors
    }

    return render(request, "pages/about.html", context)