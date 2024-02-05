from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from .serializer import UserSerializer
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from .models import User
from datetime import datetime, timedelta
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Credenciales inválidas. Por favor, inténtalo de nuevo.',
        'inactive': 'Esta cuenta está inactiva.',
    }

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user-list') 
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

class UserListView(UserPassesTestMixin, ListView):
    model = User
    template_name = 'user_list.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

    def get_queryset(self):
        return User.objects.all()

    def post(self, request, *args, **kwargs):
        if 'delete_user' in request.POST:
            user_id = request.POST.get('delete_user')
            user = get_object_or_404(User, pk=user_id)
            user.delete()
        elif 'edit_user' in request.POST:
            user_id = request.POST.get('edit_user')
            user = get_object_or_404(User, pk=user_id)
            return render(request, 'user_edit.html', {'user': user})

        return redirect('user-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now().date()

        context['users_with_due_dates'] = [
            (user, user.fecha_de_entrada + timedelta(days=user.dias_abonados))
            if user.fecha_de_entrada is not None and user.dias_abonados is not None
            else (user, None)
            for user in context['object_list']
        ]

        return context

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def user_logout(request):
    logout(request)
    return redirect ('login')

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('user-list') 