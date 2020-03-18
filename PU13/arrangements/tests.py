import unittest

from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve

from .models import Challenge, KnitNight
from .views import *
from .forms import *


# Create your tests here.
class TestUrls(TestCase):

    # Tests the url for challengeView
    def test_arr_url_resolves(self):
        url = reverse('chall')
        self.assertEquals(resolve(url).func, challengeView)

    # Tests the url for challenge_detail
    def test_challenge_detail_url_resolves(self):
        url = reverse('challenge_detail', args=['1'])
        self.assertEquals(resolve(url).func, challenge_detail)

    # Tests the url for create_challenge
    def test_create_challenge_url_resolves(self):
        url = reverse('create_challenge')
        self.assertEquals(resolve(url).func, create_challenge)

    # Tests the url for knit
    def test_knitView_url_resolves(self):
        url = reverse('knit')
        self.assertEquals(resolve(url).func, knitView)

    # Tests the url for create_knit
    def test_create_knit_url_resolves(self):
        url = reverse('create_knit')
        self.assertEquals(resolve(url).func, create_knit)

    # Tests the url for knit_detail
    def test_knit_detail_url_resolves(self):
        url = reverse('knit_detail', args=['1'])
        self.assertEquals(resolve(url).func, knit_detail)

    # Tests the url for my_page
    def test_my_page_url_resolves(self):
        url = reverse('my_page')
        self.assertEquals(resolve(url).func, my_page)

    # Tests the url for deregister_challenge - Can't get this to work properly.
    # def test_deregister_challenge_url_resolves(self):

    # Tests the url for deregister_challenge - Can't get this to work properly
    # def test_deregister_knit_url_resolves(self):

    # Tests the url for complete_challenge - Can't get this to work properly
    # def test_complete_challenge_url_resolves(self):


#class ArrangementsTesting(TestCase):

#    @classmethod
#    def setUp(self):
#        Challenge