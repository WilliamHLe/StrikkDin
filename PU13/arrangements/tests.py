from django.test import TestCase, Client

# Create your tests here.
from django.urls import resolve, reverse
from .views import challengeView, knitView, my_page, create_knit, create_challenge, complete_challenge, \
    challenge_detail, knit_detail, deregister_challenge, deregister_knit


# Tester for utfordringer
class TestChallenge(TestCase):
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


# Tester for strikkekveld
class TestKnitNight(TestCase):
    def setUp(self):

        self.strikkekveld_url = reverse("knit")
        self.strikkekveld_opprett_url = reverse("create_knit")
        # Må legge til argumenter for å at urlen skal finnes
        self.strikkekveld_detaljer_url = reverse("knit_detail", args=[4])

    def test_url(self):
        self.assertEquals(resolve(self.strikkekveld_url).func, knitView)
        self.assertEquals(resolve(self.strikkekveld_opprett_url).func, create_knit)
        self.assertEquals(resolve(self.strikkekveld_detaljer_url).func, knit_detail)


# Tester for min side
class TestMyPage(TestCase):
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
