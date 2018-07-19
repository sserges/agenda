# -*-coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Evenement(models.Model):
    """
    Cette classe renferme toutes les informations d'un événement.
    - un nom pour le retrouver facilement
    - une description pour enregistrer toutes les informations annexes de cet événement
    - les participants, qui sont des utilisateurs
    Les informations supplémentaires sur les participants à cet évènement sont stockées sur le
    modèle Evenement_Participant.
    - la date à laquelle se déroule l'événement
    - le lieu de l'événement (pour le moment, il s'agit uniquement d'un champ texte, mais un 
    vrai champ "géographique" serait sans doute plus utile).

    # Création d'un événement.
    # On importe datetime et timedelta pour manipuler les objets dates.
    # On importe également le modèle User de Django pour insérer un participant.
    >>> from datetime import datetime, timedelta
    >>> # Commencez par créer un objet Evenement.
    >>> evenement = Evenement()
    >>> evenement.nom = "Rendez-vous chez le dentiste"
    >>> evenement.description = "Pas très agréable :("
    >>> evenement.date = datetime.now() + timedelta(days=5)
    >>> evenement.lieu = "Chez le dentiste"
    >>> # Sauvegardez l'objet Evenement.
    >>> evenement.save()
    >>> # Vérifiez que l'objet a bien été créé.
    >>> rendezvous = Evenement.objects.get(lieu="Chez le dentiste")
    >>> print(rendezvous)
    Evenement object
    >>> # Vérifiez l'un des champs de l'objet.
    >>> rendezvous.nom
    'Rendez-vous chez le dentiste'
    """
    nom = models.CharField(max_length=250)
    description = models.TextField()
    participants = models.ManyToManyField(User, through="Evenement_Participant")
    date = models.DateTimeField()
    lieu = models.TextField()


class Evenement_Participant(models.Model):
    evenement = models.ForeignKey(Evenement)
    participant = models.ForeignKey(User)
    status_choices = (
        (0, "hôte"),
        (1, "invité"),
        (2, "désisté")
    )
    status = models.IntegerField(choices=status_choices)
