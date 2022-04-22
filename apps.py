from django.apps import AppConfig


class RegistrousuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'RegistroUsuario'

    def ready(self):
        import RegistroUsuario.signals
