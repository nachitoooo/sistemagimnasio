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
    path('user-list/', UserListView.as_view(), name='user-list'),  
    path('login/', login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('user-edit/<int:pk>/', UserUpdateView.as_view(), name='user-edit'),  # Agrega esta línea

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
