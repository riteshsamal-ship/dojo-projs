from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path("quotes/create", views.create_quote),
    path('quotes/<int:quote_id>/', views.show_one),
    path('quotes/<int:quote_id>/delete', views.delete),
    path('quotes', views.quotes),
    path('edit', views.edit),
    path('update', views.update)

]