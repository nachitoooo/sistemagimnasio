from django.urls import path, include
from rest_framework import routers
from api import views
from .views import UserListView, UserUpdateView, login_view
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'User', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user-list/', UserListView.as_view(), name='user-list'),  # Corregir aquí
    path('user-edit/<int:pk>/', UserUpdateView.as_view(), name='user-edit'),
    path('login/', login_view, name='login'),  # Corregir aquí
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
