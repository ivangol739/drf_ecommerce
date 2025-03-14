from django.urls import path

from apps.sellers.views import SellersView, ProductsBySellerView,SellerProductView

urlpatterns = [
    path("", SellersView.as_view()),
    path("products/", ProductsBySellerView.as_view()),
    path("products/<slug:slug>/", SellerProductView.as_view()),
]