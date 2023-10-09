from django.apps import AppConfig

class upticketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'upticket'

    def ready(self):
        import upticket.signals  # Reemplaza 'tu_app' por el nombre de tu aplicación

