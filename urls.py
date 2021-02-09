from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shophome"),
    path('about/', views.about, name="AboutUS"),
    path('contact/', views.contact, name="contactus"),
    path('tracker/', views.tracker, name="tracker"),
    path('search/', views.search, name="search"),
    path('products/<int:myid>', views.prodview, name="prodview"),
    path('checkout/', views.checkout, name="checkout"),
    path('category/', views.category, name="category"),
    path('predictimage/', views.predictimage, name="predictimage"),
]
