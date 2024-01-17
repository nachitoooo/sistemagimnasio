from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UserSerializer
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy
from .models import User
from datetime import datetime, timedelta

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'

    def get_queryset(self):
        return User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now().date()

        # Combina object_list y due_dates en una lista de tuplas
        context['users_with_due_dates'] = list(zip(context['object_list'], [
            user.fecha_de_entrada + timedelta(days=user.dias_abonados) 
            if user.fecha_de_entrada is not None and user.dias_abonados is not None 
            else None 
            for user in context['object_list']
        ]))
        
        return context

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    from django.shortcuts import render

class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('user-list')  # Nombre de la URL para la lista de usuarios

