from django.db import models

class Inscription(models.Model):
    CHOICES_TYPE = [
        ('licence_twin', 'LICENCE TWIN'),
        ('licence_srit', 'LICENCE SRIT'),
        ('master_informatique', 'MASTER INFORMATIQUE')
    ]
    
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    niveau_etude = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    etablissement_origine = models.CharField(max_length=200)
    concours_souhaiter = models.CharField(max_length=150, choices=CHOICES_TYPE)

    extrait_naissance = models.FileField(upload_to='documents/extrait/')
    certificat_nationalite = models.FileField(upload_to='documents/certificat/')
    lettre_motivation = models.FileField(upload_to='documents/lettre/')
    diplome = models.FileField(upload_to='documents/diplome/')
    photo = models.ImageField(upload_to='documents/photo/')

    date_inscription = models.DateTimeField(auto_now_add=True)
    numero_inscription = models.CharField(max_length=100, unique=True, blank=True)
    is_confirmed = models.BooleanField(default=False)



    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.numero_inscription}"
