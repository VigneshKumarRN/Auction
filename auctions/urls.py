from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("Auctionlisting/<str:listing_id>", views.Auctionlisting, name="Auctionlisting"),
    path("remove_watchlist/<str:listing_id>", views.remove_watchlist, name="remove_watchlist"),
    path("add_watchlist/<str:listing_id>", views.add_watchlist, name="add_watchlist"),
    path("bidding/<str:listing_id>", views.bidding, name="bidding"),
    path("close_bidding/<str:listing_id>", views.close_bidding, name="close_bidding"),
    path("watch_list/<str:user_id>", views.watchlist, name="watchlist"),
    path("categories", views.category, name="categories")
]
