from django.shortcuts import render, redirect
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
            return redirect('user-list')  # Utiliza la URL directamente
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now().date()

        # Combina object_list y due_dates en una lista de tuplas
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

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('user-list') 
