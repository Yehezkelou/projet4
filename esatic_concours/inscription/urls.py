from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewInscriptionView.as_view(), name='inscription_form'),
    path('confirmation/<int:pk>/', views.InscriptionConfirmView.as_view(), name='inscription_confirmation'),
    path('felicitation/', views.InscriptionSuccessView.as_view(), name='inscription_success'),
]
