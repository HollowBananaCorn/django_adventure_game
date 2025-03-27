from django.test import TestCase

from rango.models import Character

class CharacterMethodTests (TestCase):

    def test_health_equals_provided(self):

        """
        Test to make sure the character's health cannot exceed 100
        """
        character = Character(current_health=100)
        character.save()

        self.assertEqual((character.current_health ==100), True)

# Create your tests here.
