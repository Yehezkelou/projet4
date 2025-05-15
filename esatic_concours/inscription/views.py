from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from django.contrib import messages
from .models import Inscription
from .forms import InscriptionForm

class NewInscriptionView(View):
    def get(self, request):
        # Affiche le formulaire d'inscription
        form = InscriptionForm()
        return render(request, 'inscription.html', {'form': form})

    def post(self, request):
        # Traite la soumission du formulaire
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            inscription = form.save(commit=False)
            inscription.is_confirmed = False  # Marque comme non confirmé
            inscription.save()  # Sauvegarde pour obtenir un ID

            # Génère le numero_inscription si ce n'est pas déjà fait
            if not inscription.numero_inscription:
                inscription.numero_inscription = f"ESATIC-{inscription.concours_souhaiter}-{inscription.id}"
                inscription.save()

            # Redirige vers la page de confirmation avec l'ID de l'inscription
            return redirect(reverse('inscription_confirmation', kwargs={'pk': inscription.pk}))
        return render(request, 'inscription.html', {'form': form})

class InscriptionConfirmView(View):
    def get(self, request, pk):
        # Affiche les données de l'inscription pour confirmation
        inscription = get_object_or_404(Inscription, pk=pk, is_confirmed=False)
        form = InscriptionForm(instance=inscription)
        return render(request, 'confirmation.html', {'form': form})

    def post(self, request, pk):
        # Marque l'inscription comme confirmée
        inscription = get_object_or_404(Inscription, pk=pk, is_confirmed=False)
        inscription.is_confirmed = True
        inscription.save()
        messages.success(request, 'Votre inscription a été confirmée avec succès.')
        return redirect('inscription_success')

class InscriptionSuccessView(View):
    def get(self, request):
        # Affiche la page de succès après confirmation
        return render(request, 'felicitation.html')
