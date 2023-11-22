from django.apps import AppConfig


class GameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'solodungeon.game'

    def ready(self):
        # Import and run any startup code here, such as signal registration
        pass
