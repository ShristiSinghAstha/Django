from urllib import response
from django.test import TestCase


class HomeTest(TestCase):
    
    def test_home(self):
        self.assertEqual(2+2,4)
        self.assertTrue(5>1)
        self.assertFalse(3==4)
        
class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get("/")
        self.assertContains(response, "Welcome to the Home Page")

def test_about_page(self):
    response = self.client.get("/about/")
    self.assertEqual(response.status_code, 200)

