from django.test import TestCase

from rango.models import Character
from rango.models import UserProfile
from rango.models import Enemy
from rango.models import Action
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
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

        enemy = Enemy()
        enemy.save()

        self.assertEqual(enemy.__str__(), enemy.name)

    def test_imageUrl_method(self):

        enemy = Enemy()
        enemy.save()

        self.assertEqual(enemy.getImageUrl(), "/static/enemy_images/"+ enemy.image_filename)

class ActionTests(TestCase):

    def test_str_method(self):

        action = Action()
        action.save()

        self.assertEqual(action.__str__(), action.name)


class IndexViewTests(TestCase):

    def test_index_view_status_code(self):

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_response_contains(self):

        response = self.client.get(reverse('rango:index'))
        self.assertContains(response, "Adventure Game Home")

    def test_uses_correct_template(self):

        response = self.client.get(reverse('rango:index'))
        self.assertTemplateUsed(response, 'rango/index.html')

    def test_index_view_context_not_logged_in(self):

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.context['boldmessage'], "not logged in")

    def test_index_view_context_logged_in(self):

        test_user = User.objects.create_user(username="Jack")
        userProfile = UserProfile(user=test_user)
        userProfile.save()

        self.client.force_login(test_user)

        response = self.client.get(reverse('rango:index'))
        self.assertEqual(response.context['boldmessage'], "Welcome to your personal game dashboard!")
        
# Create your tests here.
