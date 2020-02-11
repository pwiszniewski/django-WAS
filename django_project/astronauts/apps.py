from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AstronautsConfig(AppConfig):
    name = 'astronauts'
    verbose_name = _("Astronauts App")
