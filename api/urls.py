from django.urls import path, include
from rest_framework import routers
from api import views
from .views import UserListView, UserUpdateView


router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-list/', UserListView.as_view(), name='user-list'),
    path('user-edit/<int:pk>/', UserUpdateView.as_view(), name='user-edit'),
]
