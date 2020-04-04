from django.forms import ModelForm

from .models import Changelog


class ChangelogForm(ModelForm):
    class Meta:
        model = Changelog
        exclude = ['userid']
