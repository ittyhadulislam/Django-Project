from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import prices, bedrooms, states

def listings(request):
    listings = Listing.objects.all().filter(is_published=True)

    peginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = peginator.get_page(page)

    context = {
        "listings": paged_listings 
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        "listing": listing
    }

    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
    # city
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)
    # state
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            queryset_list = queryset_list.filter(state__iexact = state)
    # price
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            queryset_list = queryset_list.filter(price__lte = price)
    context = {
        "states": states,
        "prices": prices,
        "listings": queryset_list,
        "bedrooms": bedrooms,
        "values": request.GET
    }

    return render(request, 'listings/search.html', context)