import unittest

from django.contrib import messages
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client

from .models import Inquiries
from .forms import SendMessageToAdmin


class InquiriesTesting(TestCase):
    @classmethod
    def setUp(self):
        self.kontakt_url = reverse("inquiries:kontakt")

    def test_valid_input_test(self):
        message_form = {
            'text_from': 'Vivi',
            'subject': 'Hjelp',
            'description': 'Blah Blah Blah'
        }
        form = SendMessageToAdmin(data=message_form)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_feedback_response(self):
        message_form = {
            'text_from': 'Vivi',
            'subject': 'Hjelp',
            'description': ''
        }
        form = SendMessageToAdmin(data=message_form)
        print(form.errors)
        response = self.client.post(self.kontakt_url, message_form)

        print(response.wsgi_request)

       # self.assertEquals('Melding sendt!',messages.success(response, 'Melding sendt!'))
        






