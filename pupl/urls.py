# pulp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Rota para a página inicial (formulário)
    path('', views.home_view, name='home'),
    
    # Rota para a página de resultados
    path('resultados/', views.results_view, name='results'),
]