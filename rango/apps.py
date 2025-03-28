from django.apps import AppConfig


class RangoConfig(AppConfig):
    name = 'rango'

    def ready(self):
        import rango.signals #making sure singnal recivers are registered