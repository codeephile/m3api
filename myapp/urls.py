from django.urls import path

from myapp.views.categories_views import (
    categories_list,
    categories_create,

)

urlpatterns = [

    path('categories/', categories_list, name='categories_list'),
    path('categories/create/', categories_create, name='categories_create'),

]
