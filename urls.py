from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('results',views.results),
    path('view_results',views.view_results)
]
