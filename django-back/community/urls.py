from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path("", views.board_list_or_create),
    path('<int:board_pk>/', views.board_detail_or_update_or_delete),
    path('<int:board_pk>/board_comment_list_or_create/', views.board_comment_list_or_create),
    path('<int:board_comment_pk>/board_comment_delete/', views.board_comment_delete),
]