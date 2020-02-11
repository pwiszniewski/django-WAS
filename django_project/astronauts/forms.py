from django import forms

from astronauts.models import Astronaut


class PersonForm(forms.ModelForm):
    class Meta:
        model = Astronaut
        fields = ['first_name', 'last_name']
