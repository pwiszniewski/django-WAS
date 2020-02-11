from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ContactsConfig(AppConfig):
    name = 'contacts'
    verbose_name = _("Contact App")
