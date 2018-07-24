from django.test import TestCase, Client
from django.contrib.auth.models import User

class StatusTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_public(self):
        urls = [
            {
                'url':'/accounts/login/',
                'status':200,
                'template':'registration/login.html'
            },
            {
                'url':'/accounts/logout/',
                'status':302,
                'template':'registration/login.html'
            },
            {
                'url':'/accounts/profile/',
                'status':302,
                'template':'registration/login.html'
            }
        ]

        for elem in urls:
            response = self.client.get(elem['url'])
            self.assertEqual(response.status_code, elem['status'])
            response = self.client.get(elem['url'], follow=True)
            self.assertEqual(response.template_name[0], elem['template'])
    
    def test_create_user(self):
        response = self.client.post('/user/create_account/', {
            'username':'john',
            'password1':'trytoguess',
            'password2':'trytoguess'
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username="john")
        self.assertEqual(user.username, "john")
    
    def test_login(self):
        self.test_create_user()
        response = self.client.post('/accounts/login/', {
            'username':'john',
            'password':'trytoguess'
        }, follow=True)

        self.assertEqual(response.status_code, 200)