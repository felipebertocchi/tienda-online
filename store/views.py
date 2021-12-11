from django.shortcuts import redirect, render
from .models import Product


def store(request):
    queryset = Product.objects.all()  # list of objects
    context = {
        "page_title": "Product List",
        "product_list": queryset
    }
    return render(request, 'store.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)


def search(request):
    if request.GET["query"]:
        search_query = request.GET["query"]
        search_results = Product.objects.filter(name__icontains=search_query)
        context = {
            "query" : search_query,
            "search_results" : search_results
        }
        return render(request, 'search.html', context)
    else:
        return redirect('store')

def featured(request):
    context = {}
    return render(request, 'featured.html', context)
