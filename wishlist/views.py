from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from .forms import WishForm
from .models import Wish

def wishlist(request):	
	wishes = Wish.objects.all()
	return render(request, "wishlist/wishlist.html", context={"wishes": wishes})

def new_wish(request):
	form = WishForm
	return render(request, "wishlist/new_wish.html", {"form": form})


class WishDetails(View):

	def get(self, request, id):
		wish = Wish.objects.get(id = id)
		return render(request, "wishlist/wish_details.html", {"wish": wish})


class NewWish(View):

	def get(self, request):
		form = WishForm
		return render(request, "wishlist/new_wish.html", {"form": form})

	def post(self, request):
		form = WishForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("wishlist_url")
		return render(request, "wishlist/new_wish.html", context={"form": form})


class WishUpdate(View):

	def get(self, request, id):
		wish = Wish.objects.get(id = id)
		form = WishForm(instance = wish)
		return render(request, "wishlist/wish_update.html", context={"form": form, "wish": wish, "id": id})

	def post(self, request, id):
		wish = Wish.objects.get(id = id)
		form = WishForm(request.POST, instance = wish)
		if form.is_valid():
			form.save()
			return redirect("wish_details_url", id=wish.id)
		return render(request, "wishlist/wish_update.html", context={"form": form})


class WishDelete(View):

	def get(self, request, id):
		wish = Wish.objects.get(id = id)
		return render(request, "wishlist/wish_delete.html", context={"wish": wish})

	def post(self, request, id):
		wish = Wish.objects.get(id = id)
		wish.delete()
		wishes = Wish.objects.all()
		return render(request, "wishlist/wishlist.html", context={"wishes": wishes})