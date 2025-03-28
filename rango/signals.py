from django.dispatch import Signal, receiver
from .models import Achievement, Character, UserProfile

achievement_check = Signal(providing_args=["user_profile", "event_type", "data"])

@receiver(achievement_check)
def check_achievements(sender, **kwargs):
    user_profile = kwargs.get("user_profile")
    event_type = kwargs.get("event_type")
    data = kwargs.get("data", {})

    if event_type == "enemy_killed":
        # increase kill counts (this should already be handled in battle logic too)
        user_profile.total_kills += 1
        user_profile.save()

        # achievement for first enemy kill.
        if user_profile.total_kills == 1:
            Achievement.objects.create(
                user=user_profile,
                name="First Kill",
                description="Defeated your first enemy!"
            )
        # cumulative achievement for 500 enemy kills.
        if user_profile.total_kills == 500:
            Achievement.objects.create(
                user=user_profile,
                name="Monster Slayer",
                description="Defeated 500 enemies over many runs!"
            )
        # If the enemy was a boss, update boss kill count.
        is_boss = data.get("is_boss", False)
        if is_boss:
            user_profile.total_boss_kills += 1
            user_profile.save()
            if user_profile.total_boss_kills == 1:
                Achievement.objects.create(
                    user=user_profile,
                    name="Boss Conqueror",
                    description="Defeated a boss for the first time!"
                )
            if user_profile.total_boss_kills == 20:
                Achievement.objects.create(
                    user=user_profile,
                    name="Relentless Boss Fighter",
                    description="Defeated the boss 20 times!"
                )
