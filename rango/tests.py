from django.test import TestCase

from rango.models import Character
from rango.models import UserProfile
from rango.models import Enemy
from rango.models import Action
from django.contrib.auth.models import User
from django.urls import reverse

class CharacterMethodTests (TestCase):

    def test_for_defaults(self):

        """
        Test to validate all values default correctly
        """

        character = Character()
        character.save()

        self.assertEqual((character.current_health == 100), True)
        self.assertEqual((character.attack == 10), True)
        self.assertEqual((character.defense == 10), True)
        self.assertEqual((character.agility == 5), True)
        self.assertEqual((character.gold == 0), True)

    def test_for_correct_str_method(self):

        """
        Validating the __str__ method
        """

        user = User.objects.create_user(username="Jack")
        userProfile = UserProfile(user=user)
        userProfile.save()

        character = Character(user=userProfile)
        character.save()

        self.assertEqual(character.__str__(), "Jack's Character")

class EnemyTests(TestCase):


    def test_str_method(self):

        """
        Enemy str method test
        """

        enemy = Enemy()
        enemy.save()

        self.assertEqual(enemy.__str__(), enemy.name)

    def test_imageUrl_method(self):

        """
        Enemy imageUrl method test
        """

        enemy = Enemy()
        enemy.save()

        self.assertEqual(enemy.getImageUrl(), "/static/enemy_images/"+ enemy.image_filename)

class ActionTests(TestCase):

    def test_str_method(self):
        
        """
        Action str method test
        """

        action = Action()
        action.save()

        self.assertEqual(action.__str__(), action.name)


class IndexViewTests(TestCase):

    def test_index_view_status_code(self):
        
        """
        Test to check that the index page loads
        """

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_response_contains(self):
        
        """
        Test to ensure correct content included in response
        """

        response = self.client.get(reverse('rango:index'))
        self.assertContains(response, "Adventure Game Home")

    def test_uses_correct_template(self):
        
        """
        Test to ensure that the correct html template was loaded
        """

        response = self.client.get(reverse('rango:index'))
        self.assertTemplateUsed(response, 'rango/index.html')

    def test_index_view_context_not_logged_in(self):
        
        """
        Testing index page behaviour of when user is not logged in
        """

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.context['boldmessage'], "not logged in")

    def test_index_view_context_logged_in(self):
        
        """
        Testing index page behaviour of logged in user
        """

        test_user = User.objects.create_user(username="Jack")
        userProfile = UserProfile(user=test_user)
        userProfile.save()
        self.client.force_login(test_user)

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.context['boldmessage'], "Welcome to your personal game dashboard!")

class LoginViewTests(TestCase):
    
    def test_login_view_status_code(self):
        
        """
        Test to check that the login page loads
        """

        response = self.client.get(reverse('rango:login'))
        self.assertEqual(response.status_code, 200)


    def test_login_renders_properly(self): 

        """
        Test to check content is loaded correctly in login page
        """       

        response = self.client.get(reverse('rango:login'))
        self.assertContains(response, "background")
    
    def test_uses_correct_template(self):
        
        """
        Test to check that correct html form is used
        """

        response = self.client.get(reverse('rango:login'))
        self.assertTemplateUsed(response, "rango/login.html")


class UserFormTests(TestCase):

    def test_form_created_with_valid_data(self):
        
        """
        Test to ensure that when user provides valid data, a user object is created
        """

        form_data = {'username':'Jackson3',
                     'email':'jack@hotmail.com',
                     'password': 'mdfa234xjei2'}
        
        response = self.client.post(reverse('rango:register'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username="Jackson3").exists())
    
    def test_form_not_created(self):

        """
        Test to see if invalid information in a form is handled correctly. Form should 
        not be created and form returned in response to correct errors
        """

        test_user = User.objects.create_user(username='Jack')
        userProfile = UserProfile(user=test_user)
        userProfile.save()

        form_data = {'username': 'Jack',
                     'email':'jack@hotmail.com',
                     'password': 'rlkfae2p1'}
        
        response = self.client.post(reverse('rango:register'), data=form_data)
        self.assertTrue("user_form" in response.context)
