from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.Test.as_view(), name = "test"),
    path('matches/', views.MatchList.as_view(), name = "match-list"),
    path('mathces/<int:pk>/', views.MatchDetail.as_view(), name = "match-detail")
]