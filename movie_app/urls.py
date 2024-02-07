from django.urls import path
from . import views

urlpatterns = [
    # path('test/', views.test_api_view),
    path('directors/', views.director_list_api_view),
    path('directors/<int:id>/', views.director_detail_api_view),
    path('movies/', views.movie_list_api_view),
    path('movies/<int:id>/', views.movie_detail_api_view),
    path('reviews/', views.review_list_api_view),
    path('reviews/<int:id>/', views.review_detail_api_view),
    path('movies/reviews/', views.review_stars_api_view),
    path('movielist/', views.MovieListCreateAPIView.as_view()),
    path('directlist/', views.DirectorListCreateAPIView.as_view()),
    path('reviewlist/', views.ReviewListCreateAPIView.as_view()),
]