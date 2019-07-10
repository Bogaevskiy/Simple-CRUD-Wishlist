from django.urls import path

from .views import *

urlpatterns = [
	path('', wishlist, name = "wishlist_url"),
	path('new_wish', NewWish.as_view(), name = "new_wish_url"),
	path('<int:id>', WishDetails.as_view(), name = "wish_details_url"),
	path('<int:id>/update', WishUpdate.as_view(), name = "wish_update_url"),
	path('<int:id>/delete', WishDelete.as_view(), name = "wish_delete_url"),
]

