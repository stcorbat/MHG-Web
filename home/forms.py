from django.forms import ModelForm

from .models import Changelog, SoundDef


class ChangelogForm(ModelForm):
    class Meta:
        model = Changelog
        exclude = ['userid']


class SoundDefForm(ModelForm):
    class Meta:
        model = SoundDef
        exclude = ['userid']
