from django.dispatch import Signal, receiver
from .models import Achievement, Character

achievement_check = Signal(providing_args=["character", "event_type", "data"])

@receiver(achievement_check)
def check_achievements(sender, **kwargs):
    character = kwargs.get("character")
    event_type = kwargs.get("event_type")
    data = kwargs.get("data", {})

    if event_type == "enemy_killed":
        # increase kill counts (this should already be handled in battle logic too)
        character.total_kills += 1
        character.save()

        # achievement for first enemy kill.
        if character.total_kills == 1:
            Achievement.objects.create(
                character=character,
                name="First Kill",
                description="Defeated your first enemy!"
            )
        # cumulative achievement for 500 enemy kills.
        if character.total_kills == 500:
            Achievement.objects.create(
                character=character,
                name="Monster Slayer",
                description="Defeated 500 enemies over many runs!"
            )
        # If the enemy was a boss, update boss kill count.
        is_boss = data.get("is_boss", False)
        if is_boss:
            character.boss_kills += 1
            character.save()
            if character.boss_kills == 1:
                Achievement.objects.create(
                    character=character,
                    name="Boss Conqueror",
                    description="Defeated a boss for the first time!"
                )
            if character.boss_kills == 20:
                Achievement.objects.create(
                    character=character,
                    name="Relentless Boss Fighter",
                    description="Defeated the boss 20 times!"
                )
