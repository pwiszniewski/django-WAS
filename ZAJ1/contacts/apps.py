from django.apps import AppConfig
from django.utils.translation import gettext_lazy

class ContactsConfig(AppConfig):
    name = 'contacts'
    verbose_name = gettext_lazy('Contact app')
