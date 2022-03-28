from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'el_galleria/index.html', {'category': 'all'})


def search(request, search_str):
    if request.method == "POST":
        input_search_str = request.POST.get('search_str', None)
        return render(request, 'el_galleria/search.html', {'category': input_search_str})
    else:
        # todo Make search request to the db, for all imgs that match the category
        return render(request, 'el_galleria/search.html', {'category': search_str})


def category(request, selected_category):
    return render(request, 'el_galleria/index.html', {'category': selected_category})

