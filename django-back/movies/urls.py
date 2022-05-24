from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.movies),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.reviews),
    path('<int:movie_pk>/reviews/create/', views.review_create),
    path('review/<int:review_pk>/', views.review_update_delete),
    path('recommend/', views.recommend),
    path('<int:movie_pk>/like/', views.movie_like),
    path('<int:movie_pk>/<int:user_pk>/like/', views.like_state),
    path('<int:movie_pk>/like/users/', views.movie_like_users),
    path('search/', views.search),
]