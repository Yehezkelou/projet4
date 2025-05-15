from django import forms
from .models import Inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = [
            'nom',
            'prenom',
            'niveau_etude',
            'email',
            'etablissement_origine',
            'concours_souhaiter',
            'extrait_naissance',
            'certificat_nationalite',
            'lettre_motivation',
            'diplome',
            'photo',
        ]
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'niveau_etude': 'Niveau d\'étude',
            'email': 'Adresse email',
            'etablissement_origine': 'Établissement d\'origine',
            'concours_souhaiter': 'Concours souhaité',
            'extrait_naissance': 'Extrait de naissance',
            'certificat_nationalite': 'Certificat de nationalité',
            'lettre_motivation': 'Lettre de motivation',
            'diplome': 'Diplôme',
            'photo': 'Photo d\'identité',
        }
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez votre nom',
                'autofocus': True,
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez votre prénom',
            }),
            'niveau_etude': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Votre niveau d\'étude actuel',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemple@domaine.com',
            }),
            'etablissement_origine': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de votre établissement d\'origine',
            }),
            'concours_souhaiter': forms.Select(attrs={
                'class': 'form-select',
            }),
            'extrait_naissance': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png',
            }),
            'certificat_nationalite': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png',
            }),
            'lettre_motivation': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx',
            }),
            'diplome': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.jpg,.jpeg,.png',
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': '.jpg,.jpeg,.png',
            }),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Exemple de validation personnalisée : vérifier si email contient un domaine spécifique
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("L'email doit être un email professionnel (example@gmail.com).")
        return email

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            if photo.size > 10*1024*1024:  # taille max 2 Mo
                raise forms.ValidationError("La photo ne doit pas dépasser 2 Mo.")
            if not photo.content_type in ['image/jpeg', 'image/png']:
                raise forms.ValidationError("Le format de la photo doit être JPEG ou PNG.")
        return photo
