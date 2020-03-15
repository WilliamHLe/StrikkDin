
from django.test import TestCase, Client
from django.urls import reverse, resolve

from .views import home

from .forms import SendMessageToAdmin
from .models import Inquiries
import json

""""
class InquiriesTesting(TestCase):
    @classmethod
    def setUp(self):
        self.kontakt_url = reverse("inquiries:kontakt")

    # tester at url-en er riktig.

    

    # tester at lovlig input passerxer gjennom
    def test_valid_input_test(self):
        message_form = {
            'text_from': 'Vivi',
            'subject': 'Hjelp',
            'description': 'Blah Blah Blah'
        }
        form = SendMessageToAdmin(data=message_form)
        print(form.errors)
        self.assertTrue(form.is_valid())

"""


class TestThisShit(TestCase):
    def setUp(self):
        self.client = Client()
        self.kontakt_url = "/kontakt/"
        self.melding1 = Inquiries.objects.create(
            text_from="hejek",
            subject="hejk",
            description="hjklkjh",
            created_at=0
        )

    def test_kontakt_url_resolves(self):
        url = reverse("kontakt")
        self.assertEquals(resolve(url).func, home)






    # Tester det å fylle ut skjemaet
    def test_inquiries_home_POST_add_new_message(self):
        response = self.client.post(self.kontakt_url, {
            "text_from": "hejek",
            "subject": "hejk",
            "description": "hjklkjh",
            "created_at": "0"
        })

        self.assertEquals(self.melding1.text_from, "hejek")

        self.assertEquals(response.status_code, 302)

        # Under vises metoden for å teste get-request
        # response = self.client.get(reverse(self.kontakt_url))
        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, "contactAdmin.html")

    def test_inquiries_home_POST_nothing(self):
        response = self.client.post(self.kontakt_url)

        self.assertEquals(response.status_code, 200)


    def test_valid_data(self):
        form = SendMessageToAdmin(data={
            "text_from": "Andreas",
            "subject": "Trenger hjelp med å legge ut annonse",
            "description": "Når jeg logger inn så får jeg masse feil med bla bla bla."
        }


        )
        self.assertTrue(form.is_valid())

    def test_not_valid_data(self):
        form = SendMessageToAdmin(data={
            "text_from": "",
            "subject": "",
            "description": ""
        })
        self.assertFalse(form.is_valid())
