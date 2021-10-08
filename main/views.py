from django.shortcuts import render, get_object_or_404
from .models import Wishlist
from datetime import datetime
from .forms import ProductForm



# Create your views here.


def index(request):
    wishlists = Wishlist.objects.all()
    return render(request, "main/index.html", {'wishlists': wishlists})


def about(request):
    return render(request, "main/about.html", {"title": "wishlist i about project"})


def list_page(request, pk):
    wishlist = get_object_or_404(Wishlist, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST)
        instance_product = form.save()
        wishlist.product.add(instance_product)
        wishlist.save()
    else:
        form = ProductForm()
    context =  {
            "wishlist": wishlist,
            # "wishlist_products": whislist.product.all()
            # "is_owner_list": wishlist.owner == request.user.username,
            "is_owner_list": True,
            "form": form
        }
    return render(request,
                  "main/wish_list.html",
                  context)



