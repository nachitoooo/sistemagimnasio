from django.urls import path, include
from rest_framework import routers
from api import views
from .views import UserListView, UserUpdateView
from .views import login_view, UserListView
from django.conf import settings
from django.conf.urls.static import static




router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-list/', UserListView, name='user-list'),
    path('user-edit/<int:pk>/', UserUpdateView.as_view(), name='user-edit'),
    path('login/', views.login_view, name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)