from django.urls import path, include
from . import views

urlpatterns = [
    path('uploadBook/',views.uploadBook,name='uploadBook'),
    path('deleteBook/<int:user_id>/<int:book_id>/',views.deleteBook,name='deleteBook'),
    path('book/<int:book_id>',views.getBook,name='getBook'),
    path('userBooks/<int:user_id>',views.getUserBooks,name='getUserBooks')
]