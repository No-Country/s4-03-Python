from django.test import TestCase

class HomePageTest(TestCase):

    def test_correct_status_home_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)
