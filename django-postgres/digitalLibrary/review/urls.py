from django.urls import path, include
from . import views

urlpatterns = [
    path('review/',views.review,name='review'),
    path('review/<int:book_id>/',views.bookReview,name='bookReview'),
]