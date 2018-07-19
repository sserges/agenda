#-*-coding:utf-8 -*-
from django.test import TestCase
from personal_calendar.models import Evenement_Participant, Evenement
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class TestEvenement_Participant(TestCase):

    def test_create_user(self):
        """
        Nous avons besoin d'un utilisateur en tant que participant à un événement, essayons d'en
        créer un.
        """
        participant1 = User(first_name="John", last_name="Doe")
        participant1.save()
        # Testons ensuite que cet élément a bien été enregistré.
        participant = User.objects.get(first_name="John")
        self.assertEqual(participant.last_name, "Doe")
    
    def test_create_event(self):
        evenement = Evenement(
            nom="Un nouvel événement",
            description="""
                Ce nouvel événement est créé pour montrer le fonctionnement des tests unitaires.
                Comme nous ne sommes plus dans une docstring, il est bien plus facile
                de faire des chaînes de caractères qui s'étendent sur plusieurs lignes.
                On peut également utiliser un format plus compact.
            """,
            date=datetime.now(),
            lieu="Un lieu quelconque"
        )

        evenement.save()
        evenement = Evenement.objects.get(nom="Un nouvel événement")
        self.assertEqual(evenement.lieu, 'Un lieu quelconque')

    def test_create_event_participant(self):
        self.test_create_user()
        self.test_create_event()
        participant = User.objects.get(first_name="John")
        evenement = Evenement.objects.get(nom="Un nouvel événement")
        evnt_part = Evenement_Participant(evenement=evenement, participant=participant, status=1)
        evnt_part.save()
        evnt = Evenement_Participant.objects.get(evenement=evenement, participant=participant)

        self.assertEqual(evnt.status, 1)