from django.urls import path
from .views import *
from .views import list, create, detail, update, delete, list, result

urlpatterns = [
    path('result/', result, name='result'),
    # path('', IndexView.as_view(), name = 'index'),
    path('', list, name = "list"),
    path('create/', create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail" ),
    path('update/<int:id>/', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
]
