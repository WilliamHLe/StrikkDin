from datetime import time, date

from django.test import TestCase, Client
import sys

from accounts.models import CustomUser

sys.path.append('..')
# Create your tests here.
from django.urls import resolve, reverse
from .views import challengeView, knitView, my_page, create_knit, create_challenge, complete_challenge, \
    challenge_detail, knit_detail, deregister_challenge, deregister_knit
from .forms import CreateChallenge, CreateKnit
from .models import Challenge, KnitNight, Ads
import os

print(os.getcwd())


# Tester for utfordringer


class TestChallengeUrl(TestCase):
    def setUp(self):
        # Ser her at vi kan bruke to måter å skrive urlen på
        self.utfordring_url = "/utfordring/"  # reverse("chall")
        self.utfordring_opprett_url = reverse("create_challenge")
        # Må legge til argumenter for å at urlen skal finnes
        self.utfordring_detaljer_url = reverse("challenge_detail", args=[123])

    def test_url(self):
        self.assertEquals(resolve(self.utfordring_url).func, challengeView)
        self.assertEquals(resolve(self.utfordring_opprett_url).func, create_challenge)
        self.assertEquals(resolve(self.utfordring_detaljer_url).func, challenge_detail)


class TestChallengeViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.chall_url = reverse("chall")
        self.utfordring_opprett_url = reverse("create_challenge")
        self.chall_detail_url = reverse("challenge_detail", args=[1])
        self.user1 = CustomUser.objects.create_user(username='test123', password='test123', name='AAron')
        self.challenge1 = Challenge.objects.create(
            challenge_name="Hansker",
            description="Hansker med avtagbare fingre",
            rec_user_level="Legende",
            created_at=date(2020, 4, 12),
            created_by=self.user1,
        )

    def test_challenge_view(self):
        response = self.client.get(self.chall_url)
        # Sjekker om den klarer å hente ned siden (HTTP-response code 200)
        self.assertEquals(response.status_code, 200)
        # Sjekker om den bruker riktig template
        self.assertTemplateUsed(response, "challenge/challenge.html")

    def test_challenge_details_get(self):
        response = self.client.get(self.chall_detail_url)
        # Sjekker om den klarer å hente ned siden (HTTP-response code 200)
        self.assertEquals(response.status_code, 200)
        # Sjekker om den bruker riktig template
        self.assertTemplateUsed((response, "challenge/challenge_detail.html"))

    def test_create_challenge(self):
        # Logger inn
        login = self.client.login(username='test123', password='test123')

        self.assertTrue(login)
        # Lager et objekt i databasen
        response = self.client.post(self.utfordring_opprett_url, {

            "challenge_name": "Heisann",
            "description": "Heiheihei",
            "rec_user_level": "Legende"}
                                    )
        # Sjekker at det er riktig http-response kode
        self.assertEquals(response.status_code, 302)
        # Sjekker at det andre objektet har navnet "Heisann" (Første objektet er det som blir laget i
        self.assertEquals(Challenge.objects.all()[1].challenge_name, "Heisann")


# Tester for selve skjemaet
class TestChallangeForm(TestCase):
    def test_valid_data(self):
        form = CreateChallenge(data={
            "challenge_name": "Verdens lengste skjerf",
            "rec_user_level": "Legende",
            "description": "Du må lage et skjerf på mer enn 5 kilometer for å slå rekorden"

        }
        )
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = CreateChallenge(data={
            "challenge_name": "",
            "rec_user_level": "",
            "description": ""
        })
        self.assertFalse((form.is_valid()))


# Tester for strikkekveld
class TestKnitNightUrl(TestCase):
    def setUp(self):
        self.strikkekveld_url = reverse("knit")
        self.strikkekveld_opprett_url = reverse("create_knit")
        # Må legge til argumenter for å at urlen skal finnes
        self.strikkekveld_detaljer_url = reverse("knit_detail", args=[4])

    def test_url(self):
        self.assertEquals(resolve(self.strikkekveld_url).func, knitView)
        self.assertEquals(resolve(self.strikkekveld_opprett_url).func, create_knit)
        self.assertEquals(resolve(self.strikkekveld_detaljer_url).func, knit_detail)


# Tester for selve skjemaet

class TestKnitForm(TestCase):
    def test_valid_data(self):
        form = CreateKnit(data={
            "knit_name": "Star Wars strikkemaraton",
            "time": date(2020, 3, 23),
            "time_start": time(19, 30, 0),
            "description": "Vi skal se alle Star Wars-filmene mens vi strikker Star Wars-figurer. Bli med, dette blir "
                           "kjempegøy!"
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = CreateKnit(data={

        })
        self.assertFalse(form.is_valid())


# Tester for min side
class TestMyPageUrl(TestCase):
    def setUp(self):
        self.min_side_url = reverse("my_page")
        self.min_side_fullført_utfordring_url = reverse("complete")
        # Må legge til argumenter for å at urlen skal finnes
        self.min_side_avmeld_utfordring_url = reverse("delete", args=[12])
        self.min_side_avmeld_strikkekveld_url = reverse("delete_knit", args=[2])

    def test_url(self):
        self.assertEquals(resolve(self.min_side_url).func, my_page)
        self.assertEquals(resolve(self.min_side_fullført_utfordring_url).func, complete_challenge)
        self.assertEquals(resolve(self.min_side_avmeld_utfordring_url).func, deregister_challenge)
        self.assertEquals(resolve(self.min_side_avmeld_strikkekveld_url).func, deregister_knit)
