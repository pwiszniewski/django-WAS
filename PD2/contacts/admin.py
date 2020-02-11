from django.contrib import admin

from contacts.models import Person, Email, Phone, Address	


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Email)
admin.site.register(Phone)
admin.site.register(Address)