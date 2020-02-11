from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    MAX_HEIGHT = 220
    MIN_HEIGHT = 100

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_UNSPECIFIED = None
    GENDER_CHOICES = [
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
        (GENDER_UNSPECIFIED, _('Unspecified'))
    ]

    first_name = models.CharField(verbose_name = _("First Name"), max_length = 30)
    last_name = models.CharField(verbose_name = _("Last Name"), max_length=30)
    date_of_birth = models.DateField(verbose_name = _("Date of Birth"), blank = True, null = True, default = None)
    pesel = models.PositiveIntegerField(verbose_name=_('PESEL'), help_text=_("Type your PESEL number"), blank = True, null = True, default = None)
    image = models.ImageField(verbose_name=_('Image'), upload_to='image/', blank = True, null = True, default = None)
    homepage = models.URLField(verbose_name=_('Homepage'), blank = True, null = True, default = None)
    notes = models.TextField(verbose_name=_('Notes'), blank = True, null = True, default = None)
    height = models.DecimalField(verbose_name=_('Height'), help_text=_('Please enter height in cm'), max_digits=4, decimal_places=1, validators=[MinValueValidator(MIN_HEIGHT), MaxValueValidator(MAX_HEIGHT)], blank = True, null = True, default = None)
    gender = models.CharField(verbose_name=_('Gender'), max_length=30, choices=GENDER_CHOICES, blank = True, null = True, default = None)
    friends = models.ManyToManyField(verbose_name=_('Firends'), to='contacts.Person', blank=True, default = None)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('People')

class Email(models.Model):
    ROLE_HOME = 'home'
    ROLE_WORK = 'work'
    ROLE_OTHER = None
    ROLE_CHOICES = [
        (ROLE_HOME, _('Home')),
        (ROLE_WORK, _('Work')),
        (ROLE_OTHER, _('Other'))
    ]
    address = models.CharField(verbose_name = _("Email Address"), max_length = 30)
    user_name = models.CharField(verbose_name = _("User Name"), max_length = 30, blank = True, null = True, default = None)
    role = models.CharField(verbose_name=_('Role'), max_length=30, choices=ROLE_CHOICES, blank = True, null = True, default = None)

    def __str__(self) -> str:
        return f'{self.address}'

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')

class Phone(models.Model):
    ROLE_HOME = 'home'
    ROLE_WORK = 'work'
    ROLE_OTHER = None
    ROLE_CHOICES = [
        (ROLE_HOME, _('Home')),
        (ROLE_WORK, _('Work')),
        (ROLE_OTHER, _('Other'))
    ]
    phone_number = models.CharField(verbose_name = _("Phone Number"), max_length = 30)
    user_name = models.CharField(verbose_name = _("User Name"), max_length = 30, blank = True, null = True, default = None)
    role = models.CharField(verbose_name=_('Role'), max_length=30, choices=ROLE_CHOICES, blank = True, null = True, default = None)

    def __str__(self) -> str:
        return f'{self.phone_number}'

    class Meta:
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')

class Address(models.Model):
    ROLE_HOME = 'home'
    ROLE_WORK = 'work'
    ROLE_OTHER = None
    ROLE_CHOICES = [
        (ROLE_HOME, _('Home')),
        (ROLE_WORK, _('Work')),
        (ROLE_OTHER, _('Other'))
    ]
    phone_number = models.CharField(verbose_name = _("Phone Number"), max_length = 30)
    user_name = models.CharField(verbose_name = _("User Name"), max_length = 30, blank = True, null = True, default = None)
    role = models.CharField(verbose_name=_('Role'), max_length=30, choices=ROLE_CHOICES, blank = True, null = True, default = None)
    street_name = models.CharField(verbose_name = _("Street Name"), max_length = 30, blank = True, null = True, default = None)
    street_number = models.PositiveIntegerField(verbose_name=_('Street Number'), blank = True, null = True, default = None)
    apartment_number = models.PositiveIntegerField(verbose_name=_('Apartment Number'), blank = True, null = True, default = None)
    postal_code = models.CharField(verbose_name = _("Postal Code"), max_length = 30, blank = True, null = True, default = None)
    city = models.CharField(verbose_name = _("City"), max_length = 30, blank = True, null = True, default = None)
    country = models.CharField(verbose_name = _("Country"), max_length = 30, blank = True, null = True, default = None)
    def __str__(self) -> str:
        return f'{self.country}'

    class Meta:
        verbose_name = _('Adress')
        verbose_name_plural = _('Adresses')