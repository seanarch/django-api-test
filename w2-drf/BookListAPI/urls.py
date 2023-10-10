from django.urls import path 
from . import views 

urlpatterns = [
    # path('books/', views.books)
    # path('books', views.BookList.as_view()),
    # path('books/<int:pk>', views.Book.as_view())
    path('menu-items', views.menu_items), 
    path('menu-items/<int:id>', views.single_item),
]