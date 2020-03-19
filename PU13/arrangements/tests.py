from django.test import TestCase, Client

# Create your tests here.
from django.urls import resolve, reverse
from .views import challengeView, knitView, my_page


class TestChallenge(TestCase):
    def setUp(self):
        self.client = Client()
        #Ser her at vi kan bruke to måter å skrive urlen på
        self.url = "/utfordring/" #reverse("chall")


    def test_url(self):
        self.assertEquals(resolve(self.url).func, challengeView)




class TestKnitNight(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("knit")

    def test_url(self):
        self.assertEquals(resolve(self.url).func, knitView)

class TestMyPage(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("my_page")

    def test_url(self):
        self.assertEquals(resolve(self.url).func, my_page)