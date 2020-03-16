from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from .views import challengeView, challenge_detail, create_challenge, deregister_challenge, my_page


# Create your tests here.
class TestUrls(SimpleTestCase):

    # Tests the url for challengeView
    def test_arr_url_resolves(self):
        url = reverse('arr')
        self.assertEquals(resolve(url).func, challengeView)

    # Tests the url for challenge_detail
    def test_challenge_detail_url_resolves(self):
        url = reverse('challenge_detail', args=['1'])
        self.assertEquals(resolve(url).func, challenge_detail)

    # Tests the url for create_challenge
    def test_create_challenge_url_resolves(self):
        url = reverse('create_challenge')
        self.assertEquals(resolve(url).func, create_challenge)

    # Tests the url for my_page
    def test_my_page_url_resolves(self):
        url = reverse('my_page')
        self.assertEquals(resolve(url).func, my_page)

    # Tests the url for deregister_challenge - Can't get this to work properly
    # def test_delete_url_resolves(self):
    #    url = resolve('deregister_challenge')
    #    self.assertEquals(reverse(url), deregister_challenge)
