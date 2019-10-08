from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image, Category

# Create your views here.
def index(request):
    images = Image.objects.all()
    categories = Category.get_all_categories()
    return render (request, 'index.html', {"images":images, "categories":categories  })


def search_results(request):
    if'searchterm' in request.GET and request.GET["searchterm"]:
        search_term=request.GET.get("searchterm")
        searched_images = Image.search_by_category(search_term)
        message= f"{search_term}"
        print(searched_images)
        return render(request,'search.html',{"message":message,"images":searched_images})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})
def category(request, id):
    categories = Category.get_all_categories()
    images = Image.objects.filter(category__id=id)
    context = {
        "categories":categories,
        "images":images
    }
    return render(request, 'category.html', context)