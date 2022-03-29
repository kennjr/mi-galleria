from django.shortcuts import render


# Create your views here.
from .models import Galleria, Location


def index(request):
    gallery = Galleria.objects.all()
    locations = Location.objects.all()
    return render(request, 'el_galleria/index.html', {'category': 'all', 'gallery': gallery, 'locations': locations})


def search(request, search_str):
    if request.method == "POST":
        input_search_str = request.POST.get('search_str', None)
        gallery = Galleria.objects.filter(category__category_str__contains=input_search_str).all()
        results_length = len(gallery)
        return render(request, 'el_galleria/search.html', {'category': input_search_str, 'gallery': gallery,
                                                           'results_len': results_length})
    else:
        results_length = 0
        return render(request, 'el_galleria/search.html', {'category': search_str, "results_len": results_length})


def category(request, selected_category):
    gallery = Galleria.objects.filter(location__name=selected_category).all()
    locations = Location.objects.all()
    results_length = len(gallery)
    return render(request, 'el_galleria/index.html', {'category': selected_category, 'gallery': gallery,
                                                      'results_len': results_length, 'locations': locations})

