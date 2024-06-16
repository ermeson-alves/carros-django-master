from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    # configuração dos receivers de signals, sobreescrevendo a função
    # herdada de AppConfig:
    def ready(self):
        import cars.signals